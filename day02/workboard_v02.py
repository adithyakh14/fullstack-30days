tasks = []
next_task_id = 1

while True:
    print("\n===== WORKBOARD =====")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. View Task Summary")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        title = input("Enter task title: ").strip()
        while title == "":
            print("Task title cannot be empty.")
            title = input("Enter task title: ").strip()

        priority = input("Enter task priority: ").strip()
        task = {
            "id": next_task_id,
            "title": title,
            "priority": priority,
            "completed": False,
        }
        tasks.append(task)
        print(f"Task {next_task_id} added.")
        next_task_id += 1

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks to display.")
        else:
            print("\n--- ALL TASKS ---")
            for task in tasks:
                if task["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"
                print(f'{task["id"]}. {task["title"]} | Priority: {task["priority"]} | Status: {status}')

    elif choice == "3":
        task_id = int(input("Enter task ID to complete: "))
        found = False
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task {task_id} marked as completed.")
                found = True
                break
        if not found:
            print(f"Task {task_id} not found.")

    elif choice == "4":
        total_tasks = len(tasks)
        completed_tasks = 0
        for task in tasks:
            if task["completed"]:
                completed_tasks += 1

        pending_tasks = total_tasks - completed_tasks
        if total_tasks > 0:
            completion_rate = completed_tasks / total_tasks * 100
        else:
            completion_rate = 0

        print("\n--- TASK SUMMARY ---")
        print(f"Total Tasks: {total_tasks}")
        print(f"Completed Tasks: {completed_tasks}")
        print(f"Pending Tasks: {pending_tasks}")
        print(f"Completion Rate: {completion_rate:.2f}%")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
