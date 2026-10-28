
import json
from pathlib import Path

file_path = Path(__file__).with_name("tasks.json")

tasks = [
    {
        "id": 1,
        "title": "Create PRD",
        "completed": True
    },
    {
        "id": 2,
        "title": "Prepare Design",
        "completed": False
    }
]

with file_path.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=4)

print("Tasks saved successfully.")

with file_path.open("r", encoding="utf-8") as file:
    loaded_tasks = json.load(file)

print("\n--- SAVED TASKS ---")

for task in loaded_tasks:
    print(f'{task["id"]}. {task["title"]} - Completed: {task["completed"]}')