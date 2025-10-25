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
