import storage
from task_logic import delete_task


def test_delete_existing_task():
    tasks = [
        {"id": 1, "title": "Create PRD", "priority": "High", "completed": False},
        {"id": 2, "title": "Design API", "priority": "Medium", "completed": False},
    ]

    result = delete_task(tasks, 1)

    assert result is True
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2


def test_delete_nonexistent_task_keeps_data_unchanged():
    tasks = [
        {"id": 1, "title": "Create PRD", "priority": "High", "completed": False}
    ]
    original_tasks = [task.copy() for task in tasks]

    result = delete_task(tasks, 99)

    assert result is False
    assert tasks == original_tasks
    assert delete_task([], 99) is False


def test_delete_preserves_remaining_ids():
    tasks = [
        {"id": 4, "title": "Create PRD", "priority": "High", "completed": False},
        {"id": 9, "title": "Design API", "priority": "Medium", "completed": False},
        {"id": 15, "title": "Write Tests", "priority": "Low", "completed": False},
    ]

    result = delete_task(tasks, 9)

    assert result is True
    assert [task["id"] for task in tasks] == [4, 15]


def test_delete_and_persist(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", test_file)
    tasks = [
        {"id": 1, "title": "Create PRD", "priority": "High", "completed": False},
        {"id": 2, "title": "Design API", "priority": "Medium", "completed": False},
    ]
    storage.save_tasks(tasks)

    result = delete_task(tasks, 1)
    if result:
        storage.save_tasks(tasks)
    loaded_tasks = storage.load_tasks()

    assert result is True
    assert test_file.exists()
    assert [task["id"] for task in loaded_tasks] == [2]
