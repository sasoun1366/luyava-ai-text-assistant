import pytest
from app import app, TASKS

@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    TASKS.clear()
    yield app.test_client()
    TASKS.clear()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_create_and_list_task(client):
    response = client.post("/api/tasks", json={"title": "Build LUYAVA agent", "description": "Test engineering workflow"})
    assert response.status_code == 201
    assert response.json["status"] == "pending"
    response = client.get("/api/tasks")
    assert response.json["count"] == 1

def test_update_task(client):
    client.post("/api/tasks", json={"title": "Initial task"})
    response = client.patch("/api/tasks/1", json={"status": "done"})
    assert response.status_code == 200
    assert response.json["status"] == "done"

def test_delete_task(client):
    client.post("/api/tasks", json={"title": "Delete me"})
    assert client.delete("/api/tasks/1").status_code == 204

def test_reject_empty_title(client):
    assert client.post("/api/tasks", json={"title": ""}).status_code == 400
