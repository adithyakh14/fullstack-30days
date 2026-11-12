import pytest

from task_lookup_refactored import build_task_index


def test_build_task_index_rejects_duplicate_ids():
    tasks = [
        {"id": 101, "title": "Create PRD", "completed": True},
        {"id": 101, "title": "Design API", "completed": False},
    ]

    with pytest.raises(ValueError, match="Duplicate task ID: 101"):
        build_task_index(tasks)
