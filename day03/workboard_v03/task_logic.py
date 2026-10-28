def add_task(tasks, title, priority):
    next_id = 1
    for task in tasks:
        if task["id"] >= next_id:
            next_id = task["id"] + 1

    new_task = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "completed": False,
    }
    tasks.append(new_task)
    return new_task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                return "already_completed"
            task["completed"] = True
            return "completed"
    return "not_found"


def calculate_summary(tasks):
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1

    pending = total - completed
    if total == 0:
        percentage = 0
    else:
        percentage = completed / total * 100
    return total, completed, pending, percentage
