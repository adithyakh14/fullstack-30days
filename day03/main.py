import calculations

total_tasks = 20
completed_tasks = 13

pending = calculations.calculate_pending(
    total_tasks, completed_tasks
)

completion_rate = calculations.calculate_completion_rate(
    total_tasks, completed_tasks
)

print(f"Pending Tasks: {pending}")
print(f"Completion Rate: {completion_rate:.2f}%")