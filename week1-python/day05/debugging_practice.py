
def calculate_completion_rate(tasks):
    completed_count = 0

    for task in tasks:
        if task["completed"]:
            completed_count += 1

    return completed_count / len(tasks) * 100


tasks = [
    {"id": 1, "title": "Create PRD", "completed": True},
    {"id": 2, "title": "Design API", "completed": True},
    {"id": 3, "title": "Test API", "completed": False}
]

rate = calculate_completion_rate(tasks)

print(f"Completion Rate: {rate:.2f}%")
