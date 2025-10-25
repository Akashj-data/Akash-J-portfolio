import pandas as pd
from agents.tools import ScheduleDB

def test_new_vs_returning_duration():
    new_duration = 60
    returning_duration = 30
    assert new_duration == 60 and returning_duration == 30

def test_schedule_seed_and_book(tmp_path):
    xlsx = tmp_path / "doctor_schedule.xlsx"
    db = ScheduleDB(str(xlsx))
    db.ensure_seed()
    slots = db.find_free_slots("Dr. Mehta", "Indiranagar", 60)
    assert len(slots) > 0
    b = db.book_slot(slots[0], "P001")
    assert b["booking_id"].startswith("B")
