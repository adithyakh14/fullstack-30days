import json
from pathlib import Path


FILE_PATH = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not FILE_PATH.exists():
        return []

    try:
        with FILE_PATH.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError("Task data is invalid JSON. No changes were saved.") from error

    if not isinstance(tasks, list):
        raise ValueError("Task data must be a list. No changes were saved.")
    return tasks


def save_tasks(tasks):
    with FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
