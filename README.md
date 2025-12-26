# Flask To-Do Application

A lightweight web application built using **Flask** to manage a To-Do list.  
The application provides **RESTful APIs for full CRUD operations**, uses **server-side templates** for the user interface, and stores data in **SQLite using explicit SQL queries (no ORM)**.

This project is designed as a clean, review-ready implementation aligned with common backend engineering best practices and the given evaluation criteria.

---

## Features

- Full CRUD operations on tasks (Create, Read, Update, Delete)
- RESTful API design with JSON request/response
- Server-rendered UI using Jinja2 templates
- SQLite database with explicit SQL (no ORM, no generic viewsets)
- Centralized logging and robust exception handling
- Automated API testing using pytest
- Clean, modular, and maintainable code structure

---

## Tech Stack

- **Language:** Python 3.9+
- **Framework:** Flask (Flask 3.x compatible)
- **Database:** SQLite
- **Templating Engine:** Jinja2
- **Testing Framework:** pytest

---

## Project Structure

flask-todo-app/
│
├── app.py
├── config.py
├── db.py
├── logger.py
├── requirements.txt
├── README.md
│
├── templates/
│ ├── base.html
│ ├── tasks.html
│ └── add_task.html
│
└── tests/
└── test_tasks_api.py


---

## Environment Setup

### Prerequisites
- Python 3.9 or higher
- Git

### Clone the Repository
```bash
git clone https://github.com/<your-username>/flask-todo-app.git
cd flask-todo-app

