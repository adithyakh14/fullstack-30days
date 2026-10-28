
tasks = []

task_count = int(input("How many tasks do you want to add? "))

for number in range(1, task_count + 1):
    task_name = input(f"Enter task {number}: ")
    tasks.append(task_name)

print("\n--- YOUR TASKS ---")

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print(f"\nFirst task: {tasks[0]}")
print(f"Last task: {tasks[-1]}")
print(f"Total tasks: {len(tasks)}")
