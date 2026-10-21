employee_name = input("Enter employee name: ")
project_name = input("Enter project name: ")
total_tasks = int(input("Enter total tasks: "))
completed_tasks = int(input("Enter completed tasks: "))
average_hours_per_task = float(input("Enter average hours per task: "))

pending_tasks = total_tasks - completed_tasks
completion_percentage = completed_tasks / total_tasks * 100
remaining_hours = pending_tasks * average_hours_per_task

print()
print("----- WORKBOARD SUMMARY -----")
print(f"Employee: {employee_name}")
print(f"Project: {project_name}")
print()
print(f"Total Tasks: {total_tasks}")
print(f"Completed Tasks: {completed_tasks}")
print(f"Pending Tasks: {pending_tasks}")
print()
print(f"Completion Rate: {completion_percentage:.2f}%")
print(f"Estimated Remaining Work: {remaining_hours:.2f} hours")
print("-----------------------------")
