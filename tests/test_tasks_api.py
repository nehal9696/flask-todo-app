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
    # Create task first
    create_resp = client.post("/api/tasks", json={
        "title": "Task to update"
    })
    assert create_resp.status_code == 201

    # Update task
    update_resp = client.put("/api/tasks/1", json={
        "title": "Updated Task",
        "status": "COMPLETED"
    })
    assert update_resp.status_code == 200


def test_delete_task(client):
    # Create task first
    create_resp = client.post("/api/tasks", json={
        "title": "Task to delete"
    })
    assert create_resp.status_code == 201

    # Delete task
    delete_resp = client.delete("/api/tasks/1")
    assert delete_resp.status_code == 200

