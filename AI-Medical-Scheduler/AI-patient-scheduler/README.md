# AI-Patient-Scheduling-Agent (skeleton)

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate  # (Windows) .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # fill creds or keep stubs
streamlit run app/streamlit_app.py
```

## What this shows
- Chat-style flow that gathers info, classifies **new vs returning**, proposes slots (**60 min for new / 30 for returning**), confirms, writes to Excel, exports an **Admin Review** file, and queues **reminders** (stubbed email/SMS clients).
- Data kept simple: `data/patients.csv`, `data/doctor_schedule.xlsx` (created on first run if absent).

## Deliverables mapping
- **Technical approach (PDF)** → summarize this architecture + choices.
- **Code Files** → this repo with notes + tests.
