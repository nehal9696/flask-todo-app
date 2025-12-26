## API Endpoints

### Create Task
POST /api/tasks
Request:
{
  "title": "Task",
  "description": "Optional",
  "due_date": "2025-01-01",
  "status": "PENDING"
}

### Get Tasks
GET /api/tasks
Response:
[
  {
    "id": 1,
    "title": "Task",
    "status": "PENDING"
  }
]
