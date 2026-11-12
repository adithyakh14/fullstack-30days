import pytest

from debugging_practice import calculate_completion_rate


def test_counts_multiple_completed_tasks():
    tasks = [
        {"completed": True},
        {"completed": True},
        {"completed": False},
    ]

    assert calculate_completion_rate(tasks) == pytest.approx(200 / 3)
