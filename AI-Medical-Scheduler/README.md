# 🩺 AI Medical Scheduling Agent

## Overview
The **AI Medical Scheduling Agent** is a smart appointment management system that automates patient booking, rescheduling, and cancellation using an AI-assisted workflow.  
It combines **LangGraph + LangChain** for agent orchestration and a **Streamlit** front-end for interactive scheduling and administrative review.  
The system integrates patient data, doctor schedules, and automated report generation into one seamless workflow.

---

## Key Features
- 🤖 Understands natural language booking requests (e.g., “Book Dr. Rao tomorrow at 5 PM”)
- 🧩 Applies **60/30-minute** scheduling rules for slot allocation
- 🕓 Checks real-time doctor availability and prevents double-bookings
- 📨 Sends appointment confirmations & reminders (Email/SMS demo stubs)
- 📊 Generates **Admin Review Excel reports** after each booking
- 💾 Maintains structured records of patients, doctors, and bookings (CSV/Excel)
- 🧠 Modular service classes for database, scheduling, exporting, and notification management

---

## Architecture Overview
The project is designed as a **modular Streamlit application** following an **agent-inspired workflow**.

### Core Modules
| Module | Description |
|---------|-------------|
| `PatientDB` | Manages patient records stored in CSV format |
| `ScheduleDB` | Tracks doctor availability and booked slots in Excel |
| `Exporter` | Generates Admin Review Excel report after every appointment |
| `EmailClient` / `SMSClient` | Handles confirmations and reminders (stubbed for demo) |
| `LangGraph Agent` | Coordinates node-based workflows (lookup, scheduling, reminders) |

### Workflow
Patient → Intake Form → Apply Scheduling Rules (60/30 mins)
→ Check Availability → Confirm Booking → Update Excel
→ Generate Admin Review → Queue Reminders

---

## Framework & Design Rationale
- **LangGraph + LangChain:** Provides a graph-based orchestration for agent logic and future extensibility to LLM-driven dialog systems.  
- **Streamlit:** Front-end for intake, scheduling, and admin control.  
- **CSV & Excel (OpenPyXL):** Lightweight persistence for data demo and analysis.  
- **Stubbed Reminders:** Demo-ready implementation using local email/SMS placeholders (can integrate with SMTP/Twilio).  

---

## Integration Details
| Integration | Implementation |
|--------------|----------------|
| Patients | 50 synthetic records stored in `patient_data.csv` |
| Doctor Schedules | Excel workbook (`doctor_schedule.xlsx`) with availability & bookings |
| Appointment Forms | Generates “New Patient Intake” PDFs post-booking |
| Reminders | Queued locally; extendable to SMTP/Twilio |
| Exports | Admin Excel report generated for every successful appointment |

---

## Technical Challenges & Solutions
| Challenge | Solution |
|------------|-----------|
| Excel file locking on Windows | Used context managers and atomic temp file replacement |
| Streamlit reruns resetting UI state | Cached slots and selections using `st.session_state` |
| Double booking risks | Filtered unavailable slots dynamically during queries |
| Notification testing without APIs | Added stubs for offline email/SMS emulation |

---

## Tech Stack
`Python` • `Streamlit` • `LangGraph` • `LangChain` • `Pandas` • `OpenPyXL` • `Dateutil`

---

## Setup & Run
```bash
# Clone repository
git clone https://github.com/Akashj-data/akash-j-portfolio.git
cd AI-Medical-Scheduler

# Install dependencies
pip install -r requirements.txt

# Launch application
streamlit run app.py

Future Enhancements

🔗 Integration with Google Calendar / Outlook API for real-time sync

🗣️ Add LLM-based conversational interface for autonomous patient interaction

🔒 Enable HIPAA-compliant secure backend for real deployments

📱 Develop mobile-first UI for patients and staff

Results & Outcomes

Fully functional AI-driven scheduling workflow

Seamless Streamlit front-end with persistent CSV/Excel data

Reduced manual scheduling effort through automation

Production-ready structure with clear separation of logic layers

