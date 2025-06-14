# 🎉 Event Management API System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-%F0%9F%9A%80-green)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Build-Complete-brightgreen.svg)]()
[![Swagger Docs](https://img.shields.io/badge/docs-Swagger-blue)](http://127.0.0.1:8000/docs)

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
├── database.py # In-memory data stores and counters
├── crud/ # CRUD
│ ├── user.py
│ ├── event.py
│ └── registration.py
├── routes/ # API route handlers
│ ├── user.py
│ ├── event.py
│ └── registration.py
├── schemas/ # Pydantic models
│ ├── user.py
│ ├── event.py
│ ├── speaker.py
│ └── registration.py
├── services/ # Business logic
│ ├── user.py
│ ├── event.py
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

```
2. Create a virtual environment (optional but recommended)

```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the application

```
uvicorn main:app --reload
```
5. Access the API docs:
```

-Swagger UI: http://localhost:8000/docs

-Redoc: http://localhost:8000/redoc
```