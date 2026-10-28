tasks = [
    {
        "id": 1,
        "title": "Build Login API",
        "assigned_to": "Rahul",
        "priority": "High",
        "completed": True,
    },
    {
        "id": 2,
        "title": "Design Dashboard",
        "assigned_to": "Priya",
        "priority": "Medium",
        "completed": False,
    },
    {
        "id": 3,
        "title": "Fix Authentication Bug",
        "assigned_to": "Rahul",
        "priority": "High",
        "completed": False,
    },
    {
        "id": 4,
        "title": "Test Database",
        "assigned_to": "Amit",
        "priority": "High",
        "completed": False,
    },
]

total_tasks = len(tasks)
completed_tasks = 0
employees = set()

for task in tasks:
    if task["completed"]:
        completed_tasks += 1
    employees.add(task["assigned_to"])

pending_tasks = total_tasks - completed_tasks
if total_tasks > 0:
    completion_rate = completed_tasks / total_tasks * 100
else:
    completion_rate = 0

print("----- WORKBOARD REPORT -----")
print()
print(f"Total Tasks: {total_tasks}")
print(f"Completed Tasks: {completed_tasks}")
print(f"Pending Tasks: {pending_tasks}")
print(f"Completion Rate: {completion_rate:.2f}%")
print()
print("Pending High Priority Tasks:")
for task in tasks:
    if task["priority"] == "High" and not task["completed"]:
        print(f'- {task["title"]}')
print()
print(f"Unique Employees: {len(employees)}")
print()
print("----------------------------")
