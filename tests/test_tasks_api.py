import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_task(client):
    response = client.post("/api/tasks", json={
        "title": "Test Task"
    })
    assert response.status_code == 201


def test_get_tasks(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_update_task(client):
    # Create task
    client.post("/api/tasks", json={"title": "Task to update"})

    # Fetch latest task ID
    tasks_resp = client.get("/api/tasks")
    task_id = tasks_resp.json[-1]["id"]

    # Update using actual ID
    response = client.put(f"/api/tasks/{task_id}", json={
        "title": "Updated Task",
        "status": "COMPLETED"
    })

    assert response.status_code == 200


def test_delete_task(client):
    # Create task
    client.post("/api/tasks", json={"title": "Task to delete"})

    # Fetch latest task ID
    tasks_resp = client.get("/api/tasks")
    task_id = tasks_resp.json[-1]["id"]

    # Delete using actual ID
    response = client.delete(f"/api/tasks/{task_id}")

    assert response.status_code == 200
