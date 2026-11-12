def add_task(tasks: list[dict], title: str, priority: str) -> dict:
    # Deleting the highest ID allows this max-plus-one scheme to reuse that ID.
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


def complete_task(tasks: list[dict], task_id: int) -> str:
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                return "already_completed"
            task["completed"] = True
            return "completed"
    return "not_found"


def delete_task(tasks: list[dict], task_id: int) -> bool:
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            return True
    return False


def calculate_summary(tasks: list[dict]) -> tuple[int, int, int, float]:
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1

    pending = total - completed
    if total == 0:
        percentage = 0.0
    else:
        percentage = completed / total * 100
    return total, completed, pending, percentage
