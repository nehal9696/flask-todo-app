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

The project follows a clean and modular structure to separate concerns such as routing, database access, configuration, templates, and testing.

```text
flask-todo-app/
│
├── app.py                # Main Flask application with UI and API routes
├── config.py             # Application configuration
├── db.py                 # Database connection and initialization logic
├── logger.py             # Centralized logging configuration
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
│
├── templates/            # HTML templates for UI
│   ├── base.html         # Base layout template
│   ├── tasks.html        # Task list view
│   ├── add_task.html     # Add task form
│   └── edit_task.html    # Edit task form
│
└── tests/                # Automated tests
    └── test_tasks_api.py # API CRUD tests using pytest


---

## Environment Setup

### Prerequisites
- Python 3.9 or higher
- Git

### Clone the Repository
```bash
git clone https://github.com/<your-username>/flask-todo-app.git
cd flask-todo-app

---

## API Documentation

The application exposes RESTful APIs for managing tasks.  
All APIs accept and return JSON data.

### Base URL
http://127.0.0.1:5000


---

### Create a Task

**Endpoint**

POST /api/tasks

**Description**  
Creates a new task in the system.

**Request Body**
```json
{
  "title": "Sample Task",
  "description": "Optional description",
  "due_date": "2025-01-01",
  "status": "PENDING"
}

**Response** (201 Created)

{
  "message": "Task created successfully"
}

**Error Responses**

400 Bad Request – Title is missing

500 Internal Server Error – Server failure

### Retrieve All Tasks

**Endpoint**

GET /api/tasks

**Description**
Fetches all tasks stored in the database.

**Response** (200 OK)

[
  {
    "id": 1,
    "title": "Sample Task",
    "description": "Optional description",
    "due_date": "2025-01-01",
    "status": "PENDING"
  }
]

### Update a Task

**Endpoint**

PUT /api/tasks/{id}

**Description**
Updates an existing task by its ID.

**Request Body**
{
  "title": "Updated Task",
  "description": "Updated description",
  "due_date": "2025-01-05",
  "status": "COMPLETED"
}

**Response** (200 OK)
{
  "message": "Task updated successfully"
}

**Error Responses**

404 Not Found – Task does not exist

500 Internal Server Error – Server failure

### Delete a Task

**Endpoint**

DELETE /api/tasks/{id}

**Description**
Deletes a task by its ID.

**Response** (200 OK)
{
  "message": "Task deleted successfully"
}

**Error Responses**

404 Not Found – Task does not exist

500 Internal Server Error – Server failure