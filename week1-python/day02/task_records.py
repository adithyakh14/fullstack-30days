
tasks = [
    {"id": 1, "title": "Build Login API", "completed": True},
    {"id": 2, "title": "Design Dashboard", "completed": False},
    {"id": 3, "title": "Test Database", "completed": False}
]

completed_count = 0

print("--- WORKBOARD TASKS ---")

for task in tasks:
    if task["completed"]:
        status = "Completed"
        completed_count += 1
    else:
        status = "Pending"

    print(f'{task["id"]}. {task["title"]} - {status}')

print(f"\nTotal Tasks: {len(tasks)}")
print(f"Completed Tasks: {completed_count}")
print(f"Pending Tasks: {len(tasks) - completed_count}")
