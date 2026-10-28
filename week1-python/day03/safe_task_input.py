while True:
    title = input("Enter task title: ").strip()
    if title:
        break
    print("Task title cannot be blank.")

while True:
    priority = input("Enter task priority (High, Medium, Low): ").strip().capitalize()
    if priority in ("High", "Medium", "Low"):
        break
    print("Priority must be High, Medium, or Low.")

while True:
    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Task ID must be a number.")
        continue

    if task_id > 0:
        break
    print("Task ID must be a positive integer.")

task = {"id": task_id, "title": title, "priority": priority}
print(f'Task {task["id"]}: {task["title"]} (Priority: {task["priority"]})')
