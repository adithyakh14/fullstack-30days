
import pytest

from task_logic import add_task, complete_task, calculate_summary


def test_add_first_task():
    tasks = []

    new_task = add_task(tasks, "Create PRD", "High")

    assert new_task["id"] == 1
    assert new_task["completed"] is False
    assert len(tasks) == 1


def test_add_task_generates_next_id():
    tasks = [
        {"id": 2, "title": "Design", "priority": "Medium", "completed": False},
        {"id": 5, "title": "Testing", "priority": "High", "completed": False}
    ]

    new_task = add_task(tasks, "Deployment", "Low")

    assert new_task["id"] == 6
    assert len(tasks) == 3


def test_complete_task():
    tasks = [
        {"id": 1, "title": "Create PRD", "priority": "High", "completed": False}
    ]

    result = complete_task(tasks, 1)

    assert result == "completed"
    assert tasks[0]["completed"] is True


def test_complete_task_twice():
    tasks = [
        {"id": 1, "title": "Create PRD", "priority": "High", "completed": True}
    ]

    result = complete_task(tasks, 1)

    assert result == "already_completed"


def test_complete_nonexistent_task():
    tasks = []

    result = complete_task(tasks, 99)

    assert result == "not_found"


def test_empty_task_summary():
    result = calculate_summary([])

    assert result == (0, 0, 0, 0)


def test_summary_with_completed_and_pending_tasks():
    tasks = [
        {"id": 1, "title": "Create PRD", "priority": "High", "completed": True},
        {"id": 2, "title": "Design", "priority": "Medium", "completed": False},
        {"id": 3, "title": "Testing", "priority": "Low", "completed": False},
    ]

    total, completed, pending, percentage = calculate_summary(tasks)

    assert total == 3
    assert completed == 1
    assert pending == 2
    assert percentage == pytest.approx(100 / 3)


def test_completing_missing_task_preserves_existing_task():
    tasks = [
        {"id": 1, "title": "Create PRD", "priority": "High", "completed": False}
    ]

    result = complete_task(tasks, 99)

    assert result == "not_found"
    assert tasks[0]["completed"] is False
