# Flask To-Do Application

A lightweight To-Do management web application built using Flask, SQLite, and RESTful APIs.

## Features
- Create and retrieve tasks via REST APIs
- Server-rendered UI using Jinja2 templates
- SQLite database (no ORM)
- Centralized logging and exception handling
- Automated API testing using pytest

## Tech Stack
- Python 3.x
- Flask
- SQLite
- pytest

## Setup Instructions

```bash
git clone https://github.com/<your-username>/flask-todo-app.git
cd flask-todo-app
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py

