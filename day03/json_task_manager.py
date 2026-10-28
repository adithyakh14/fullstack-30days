import json
from pathlib import Path


file_path = Path(__file__).with_name("workboard_tasks.json")

if file_path.exists():
    with file_path.open("r", encoding="utf-8") as file:
        tasks = json.load(file)
else:
    tasks = []

title = input("Enter task title: ")
priority = input("Enter task priority: ")

tasks.append({"title": title, "priority": priority, "completed": False})

with file_path.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=4)

print("\n--- SAVED TASKS ---")
for number, task in enumerate(tasks, start=1):
    if task["completed"]:
        status = "Completed"
    else:
        status = "Pending"
    print(f'{number}. {task["title"]} | Priority: {task["priority"]} | Status: {status}')
