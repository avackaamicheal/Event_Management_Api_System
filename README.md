# 🎉 Event Management API System

A simple backend API for managing users, events, speakers, and registrations using FastAPI. Built for educational and prototyping purposes.

---

## 🧩 Features

- ✅ User CRUD + Deactivation
- 🗓️ Event CRUD + Close Registration
- 🎤 Speaker Management (3 preloaded)
- 📝 User Registration for Events
- 📌 Attendance Tracking
- 🧠 In-memory storage using Python lists (no DB)

---

## 🏗️ Project Structure

event-management-api/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py # FastAPI app entry point
├── db.py # In-memory data stores and counters
├── routes/ # API route handlers
│ ├── user.py
│ ├── event.py
│ ├── speaker.py
│ └── registration.py
├── schemas/ # Pydantic models
│ ├── user.py
│ ├── event.py
│ ├── speaker.py
│ └── registration.py
├── services/ # Business logic
│ ├── user.py
│ ├── event.py
│ ├── speaker.py
│ └── registration.py


---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10 or higher
- pip

### 🛠️ Installation

1. Clone the repo

```bash
git clone https://github.com/avackaamicheal/Event_Management_Api_System.git
cd Event_Management_Api_System

