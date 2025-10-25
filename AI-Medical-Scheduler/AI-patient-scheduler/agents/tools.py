from __future__ import annotations
import os
from datetime import datetime, timedelta
import pandas as pd
from loguru import logger
from pydantic import BaseModel

AVAIL_SHEET = "availability"
BOOKINGS_SHEET = "bookings"

class PatientDB:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        if not os.path.exists(csv_path):
            pd.DataFrame(columns=[
                "patient_id","first_name","last_name","dob","phone","email","is_returning","insurance_carrier","member_id","group_number"
            ]).to_csv(csv_path, index=False)

    def _load(self) -> pd.DataFrame:
        return pd.read_csv(self.csv_path)

    def _save(self, df: pd.DataFrame):
        df.to_csv(self.csv_path, index=False)

    def find_or_create(self, first_name, last_name, dob, phone, email, is_returning: bool):
        df = self._load()
        match = df[(df.first_name==first_name)&(df.last_name==last_name)&(df.dob==dob)]
        if not match.empty:
            row = match.iloc[0].to_dict()
            # Update contact/returning flag if changed
            df.loc[match.index[0], ["phone","email","is_returning"]] = [phone, email, is_returning]
            self._save(df)
            return row
        new_id = f"P{len(df)+1:03}"
        row = {
            "patient_id": new_id,
            "first_name": first_name,
            "last_name": last_name,
            "dob": dob,
            "phone": phone,
            "email": email,
            "is_returning": is_returning,
            "insurance_carrier": "",
            "member_id": "",
            "group_number": "",
        }
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        self._save(df)
        return row

class ScheduleDB:
    def __init__(self, xlsx_path: str):
        self.xlsx_path = xlsx_path
        os.makedirs(os.path.dirname(xlsx_path), exist_ok=True)

    def ensure_seed(self):
        if os.path.exists(self.xlsx_path):
            return
        # Seed with 2 doctors x 2 locations with 9-17 workday slots
        rows = []
        base = datetime.now().date()
        for dname in ["Dr. Mehta","Dr. Kapoor"]:
            for loc in ["Indiranagar","HSR"]:
                for day in range(0, 7):
                    date_str = (base + timedelta(days=day)).isoformat()
                    start_times = ["09:00","10:00","11:00","12:00","14:00","15:00","16:00"]
                    for t in start_times:
                        rows.append({
                            "doctor": dname,
                            "location": loc,
                            "date": date_str,
                            "start_time": t,
                            "end_time": "",  # resolved on booking
                            "slot_minutes": 60,  # maximum block; we can split later
                            "is_booked": False,
                            "patient_id": "",
                        })
        with pd.ExcelWriter(self.xlsx_path, engine="openpyxl") as xw:
            pd.DataFrame(rows).to_excel(xw, AVAIL_SHEET, index=False)
            pd.DataFrame(columns=["booking_id","doctor","location","start","end","patient_id"]).to_excel(xw, BOOKINGS_SHEET, index=False)

    def _load(self):
        if not os.path.exists(self.xlsx_path):
            self.ensure_seed()
        xl = pd.ExcelFile(self.xlsx_path)
        avail = xl.parse(AVAIL_SHEET)
        bookings = xl.parse(BOOKINGS_SHEET)
        return avail, bookings

    def _save(self, avail: pd.DataFrame, bookings: pd.DataFrame):
        with pd.ExcelWriter(self.xlsx_path, engine="openpyxl") as xw:
            avail.to_excel(xw, AVAIL_SHEET, index=False)
            bookings.to_excel(xw, BOOKINGS_SHEET, index=False)

    def doctors(self):
        avail, _ = self._load()
        return sorted(avail["doctor"].unique().tolist())

    def locations(self):
        avail, _ = self._load()
        return sorted(avail["location"].unique().tolist())

    def find_free_slots(self, doctor: str, location: str, duration_min: int, days_ahead: int = 10):
        avail, _ = self._load()
        df = avail[(avail["doctor"]==doctor) & (avail["location"]==location) & (~avail["is_booked"]) ]
        df = df.copy()
        # Build concrete start/end timestamps for display
        slots = []
        for idx, r in df.iterrows():
            start_dt = datetime.fromisoformat(f"{r['date']} {r['start_time']}")
            end_dt = start_dt + timedelta(minutes=duration_min)
            slots.append({
                "doctor": doctor,
                "location": location,
                "start": start_dt.strftime("%Y-%m-%d %H:%M"),
                "end": end_dt.strftime("%Y-%m-%d %H:%M"),
                "row_index": idx
            })
        return slots[:10]

    def book_slot(self, slot: dict, patient_id: str):
        avail, bookings = self._load()
        idx = slot["row_index"]
        avail.loc[idx, "is_booked"] = True
        avail.loc[idx, "patient_id"] = patient_id
        # Compute end time if empty
        if not avail.loc[idx, "end_time"]:
            # Derive from slot_minutes or 30/60 policy → we use difference from provided slot
            start_dt = datetime.fromisoformat(slot["start"])
            end_dt = datetime.fromisoformat(slot["end"])
            avail.loc[idx, "end_time"] = end_dt.strftime("%H:%M")
        booking_id = f"B{len(bookings)+1:04}"
        new_b = {
            "booking_id": booking_id,
            "doctor": slot["doctor"],
            "location": slot["location"],
            "start": slot["start"],
            "end": slot["end"],
            "patient_id": patient_id,
        }
        bookings = pd.concat([bookings, pd.DataFrame([new_b])], ignore_index=True)
        self._save(avail, bookings)
        return new_b

class Exporter:
    def export_admin_review(self, booking: dict, patient: dict) -> str:
        os.makedirs("reports", exist_ok=True)
        path = f"reports/admin_review_{booking['booking_id']}.xlsx"
        df = pd.DataFrame([{
            **booking,
            "patient_name": f"{patient['first_name']} {patient['last_name']}",
            "patient_email": patient["email"],
            "patient_phone": patient["phone"],
            "is_returning": patient["is_returning"],
        }])
        with pd.ExcelWriter(path, engine="xlsxwriter") as xw:
            df.to_excel(xw, sheet_name="review", index=False)
        return path

class EmailClient:
    def __init__(self):
        self.enabled = bool(os.getenv("SMTP_HOST"))

    def send(self, to_email: str, subject: str, body: str):
        if not self.enabled:
            logger.info(f"[EMAIL:STUB] → {to_email} | {subject} | {body[:60]}...")
            return True
        # TODO: implement SMTP/SendGrid
        logger.warning("SMTP configured but send() not implemented yet.")
        return False

class SMSClient:
    def __init__(self):
        self.enabled = bool(os.getenv("TWILIO_SID"))

    def send(self, to_phone: str, message: str):
        if not self.enabled:
            logger.info(f"[SMS:STUB] → {to_phone} | {message}")
            return True
        # TODO: implement Twilio
        logger.warning("Twilio configured but send() not implemented yet.")
        return False
