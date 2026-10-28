def calculate_completion_rate(total_tasks, completed_tasks):
    if total_tasks == 0:
        return 0

    return completed_tasks / total_tasks * 100


def calculate_pending_tasks(total_tasks, completed_tasks):
    return total_tasks - completed_tasks


total = 7
completed = 3

completion_rate = calculate_completion_rate(total, completed)
pending = calculate_pending_tasks(total, completed)

print(f"Pending Tasks: {pending}")
print(f"Completion Rate: {completion_rate:.2f}%")