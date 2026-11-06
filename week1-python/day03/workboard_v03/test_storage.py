import pytest

import storage


def test_save_and_load_tasks(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", test_file)
    tasks = [
        {
            "id": 1,
            "title": "Create PRD",
            "priority": "High",
            "completed": False,
        }
    ]

    storage.save_tasks(tasks)
    loaded_tasks = storage.load_tasks()

    assert test_file.exists()
    assert loaded_tasks == tasks


def test_invalid_json_raises_value_error(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    test_file.write_text("{invalid JSON", encoding="utf-8")
    monkeypatch.setattr(storage, "FILE_PATH", test_file)

    with pytest.raises(ValueError, match="invalid JSON"):
        storage.load_tasks()


def test_missing_file_returns_empty_list(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    monkeypatch.setattr(storage, "FILE_PATH", test_file)

    assert storage.load_tasks() == []
    assert not test_file.exists()


def test_missing_task_fields_raises_value_error(tmp_path, monkeypatch):
    test_file = tmp_path / "tasks.json"
    test_file.write_text('[{"title": "Create PRD"}]', encoding="utf-8")
    monkeypatch.setattr(storage, "FILE_PATH", test_file)

    with pytest.raises(ValueError, match="missing required fields"):
        storage.load_tasks()

    test_file.write_text("[42]", encoding="utf-8")
    with pytest.raises(ValueError, match="must be a dictionary"):
        storage.load_tasks()
