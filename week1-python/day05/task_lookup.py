tasks = [
    {"id": 101, "title": "Create PRD", "completed": True},
    {"id": 102, "title": "Design API", "completed": False},
    {"id": 103, "title": "Build Backend", "completed": False},
    {"id": 104, "title": "Write Tests", "completed": False},
]


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


tasks_by_id = {}
for task in tasks:
    tasks_by_id[task["id"]] = task

print("--- TASK LOOKUP ---")
print("\nList Search:")
list_result = find_task_by_id(tasks, 103)
if list_result is not None:
    print(f'{list_result["id"]}. {list_result["title"]}')

print("\nDictionary Search:")
dictionary_result = tasks_by_id.get(103)
if dictionary_result is not None:
    print(f'{dictionary_result["id"]}. {dictionary_result["title"]}')

print("\nSearch for ID 999:")
missing_task = tasks_by_id.get(999)
if missing_task is None:
    print("Task not found.")
