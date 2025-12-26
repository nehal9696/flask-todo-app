def test_create_task(client):
    response = client.post("/api/tasks", json={
        "title": "Test Task"
    })
    assert response.status_code == 201

def test_get_tasks(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json, list)
