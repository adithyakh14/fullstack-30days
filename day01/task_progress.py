total_tasks = 20
completed_tasks = 13

pending_tasks = total_tasks - completed_tasks
completion_percentage = completed_tasks / total_tasks * 100

print(f"Total Tasks: {total_tasks}")
print(f"Completed Tasks: {completed_tasks}")
print(f"Pending Tasks: {pending_tasks}")
print(f"Completion Rate: {completion_percentage}%")