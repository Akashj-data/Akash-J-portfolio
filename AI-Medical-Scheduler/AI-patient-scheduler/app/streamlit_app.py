import os
import uuid
from datetime import datetime, timedelta

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from loguru import logger

from agents.tools import PatientDB, ScheduleDB, Exporter, EmailClient, SMSClient
# from agents.graph import run_graph  # (Optional) integrate LLM/graph later

load_dotenv()
st.set_page_config(page_title="RagaAI Patient Scheduler", page_icon="🩺", layout="centered")

@st.cache_data
def seed_patients_csv(path: str = "data/patients.csv"):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(path):
        return path
    df = pd.DataFrame([
        {
            "patient_id": f"P{i:03}",
            "first_name": f"Test{i}",
            "last_name": "User",
            "dob": f"199{i%10}-0{(i%8)+1}-15",
            "phone": f"+91-98{i:07}",
            "email": f"test{i}@example.com",
            "is_returning": bool(i % 2),
            "insurance_carrier": "AcmeHealth",
            "member_id": f"M{i:05}",
            "group_number": "G1234",
        }
        for i in range(1, 51)
    ])
    df.to_csv(path, index=False)
    return path

@st.cache_resource
def get_clients():
    patient_db = PatientDB("data/patients.csv")
    schedule_db = ScheduleDB("data/doctor_schedule.xlsx")
    exporter = Exporter()
    email = EmailClient()
    sms = SMSClient()
    return patient_db, schedule_db, exporter, email, sms

seed_patients_csv()
patient_db, schedule_db, exporter, email_client, sms_client = get_clients()

st.title("🩺 AI Patient Scheduling ")

with st.sidebar:
    st.header("Admin")
    if st.button("Initialize doctor schedule.xlsx", type="primary"):
        schedule_db.ensure_seed()
        st.success("Doctor schedule initialized.")
    st.caption("Exports → reports/admin_review_*.xlsx")

# Simple scripted flow (LLM optional)
with st.form("booking_form"):
    st.subheader("Patient intake")
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First name", "Asha")
        last_name = st.text_input("Last name", "Rao")
        dob = st.date_input("DOB")
    with col2:
        phone = st.text_input("Phone", "+91-9898989898")
        email = st.text_input("Email", "asha.rao@example.com")
        is_returning = st.selectbox("Are you a returning patient?", ["No", "Yes"]) == "Yes"

    st.subheader("Preferences")
    doctor = st.selectbox("Doctor", schedule_db.doctors())
    location = st.selectbox("Location", schedule_db.locations())
    submit = st.form_submit_button("Find slots")

if submit:
    # Lookup or create patient
    patient = patient_db.find_or_create(first_name, last_name, dob.isoformat(), phone, email, is_returning)

    duration_min = 30 if is_returning else 60
    slots = schedule_db.find_free_slots(doctor=doctor, location=location, duration_min=duration_min, days_ahead=10)

    if not slots:
        st.warning("No slots available in the next 10 days. Try another doctor/location.")
    else:
        st.success(f"Found {len(slots)} slot(s). Pick one to confirm.")
        choice = st.radio("Available slots", [f"{s['start']} → {s['end']}" for s in slots])
        if st.button("Confirm booking", type="primary"):
            idx = [f"{s['start']} → {s['end']}" for s in slots].index(choice)
            booking = schedule_db.book_slot(slots[idx], patient["patient_id"])  # writes to Excel
            # Send confirmations (stub clients print to logs / Streamlit)
            email_client.send(email, subject="Appointment Confirmation", body=str(booking))
            sms_client.send(phone, f"Confirmed: {booking['start']} with {booking['doctor']} @ {booking['location']}")

            # Export admin review
            out_path = exporter.export_admin_review(booking, patient)
            st.success("Appointment confirmed and notifications queued.")
            st.download_button("Download Admin Review", data=open(out_path, "rb").read(), file_name=os.path.basename(out_path))

            st.info("Next step: Email the New Patient Intake form link.")
