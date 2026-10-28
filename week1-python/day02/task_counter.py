employee_count = int(input("How many employees need to be processed? "))
total_completed_tasks = 0

for employee_number in range(1, employee_count + 1):
    completed_tasks = int(input(f"Tasks completed by employee {employee_number}: "))
    total_completed_tasks += completed_tasks

print(f"Total tasks completed: {total_completed_tasks}")
