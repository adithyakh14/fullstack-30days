
import pytest
from fastapi.testclient import TestClient

import main


client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_tasks(monkeypatch):
    fresh_tasks = [
        {
            "id": 1,
            "title": "Create PRD",
            "priority": "High",
            "completed": True,
        },
        {
            "id": 2,
            "title": "Develop API",
            "priority": "Medium",
            "completed": False,
        },
    ]

    monkeypatch.setattr(main, "tasks", fresh_tasks)


def test_get_all_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Task not found"
    }


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_filter_incomplete_tasks():
    response = client.get("/tasks", params={"completed": "false"})

    assert response.status_code == 200
    assert response.json() == [
        {"id": 2, "title": "Develop API", "priority": "Medium", "completed": False}
    ]


def test_create_valid_task():
    response = client.post(
        "/tasks",
        json={"title": "Write API Tests", "priority": "High"},
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 3,
        "title": "Write API Tests",
        "priority": "High",
        "completed": False,
    }
    assert client.get("/tasks/3").json() == response.json()


def test_reject_blank_title():
    response = client.post(
        "/tasks",
        json={"title": "   ", "priority": "High"},
    )

    assert response.status_code == 422
    assert response.json() == {"detail": "Title must be a nonblank string"}
    assert len(client.get("/tasks").json()) == 2


def test_complete_task():
    response = client.patch("/tasks/2", json={"completed": True})

    assert response.status_code == 200
    assert response.json() == {
        "id": 2,
        "title": "Develop API",
        "priority": "Medium",
        "completed": True,
    }
    assert client.get("/tasks/2").json()["completed"] is True


def test_reject_invalid_completion():
    response = client.patch("/tasks/2", json={"completed": False})

    assert response.status_code == 422
    assert client.get("/tasks/2").json()["completed"] is False


def test_delete_task():
    response = client.delete("/tasks/2")

    assert response.status_code == 204
    assert response.content == b""
    assert client.get("/tasks/2").status_code == 404
    assert [task["id"] for task in client.get("/tasks").json()] == [1]
