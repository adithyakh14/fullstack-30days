from storage import load_tasks, save_tasks
from task_logic import add_task, calculate_summary, complete_task


def main():
    try:
        tasks = load_tasks()
    except ValueError as error:
        print(f"Cannot start WorkBoard: {error}")
        return

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
            while not title:
                print("Task title cannot be empty.")
                title = input("Enter task title: ").strip()

            priority = input("Enter task priority (High, Medium, Low): ").strip().capitalize()
            while priority not in ("High", "Medium", "Low"):
                print("Priority must be High, Medium, or Low.")
                priority = input("Enter task priority (High, Medium, Low): ").strip().capitalize()

            task = add_task(tasks, title, priority)
            save_tasks(tasks)
            print(f'Task {task["id"]} added.')

        elif choice == "2":
            if not tasks:
                print("No tasks to display.")
            else:
                print("\n--- ALL TASKS ---")
                for task in tasks:
                    if task["completed"]:
                        status = "Completed"
                    else:
                        status = "Pending"
                    print(
                        f'{task["id"]}. {task["title"]} | '
                        f'Priority: {task["priority"]} | Status: {status}'
                    )

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
            except ValueError:
                print("Task ID must be a positive integer.")
                continue

            if task_id <= 0:
                print("Task ID must be a positive integer.")
                continue

            result = complete_task(tasks, task_id)
            if result == "completed":
                save_tasks(tasks)
                print(f"Task {task_id} marked as completed.")
            elif result == "already_completed":
                print(f"Task {task_id} is already completed.")
            else:
                print(f"Task {task_id} not found.")

        elif choice == "4":
            total, completed, pending, percentage = calculate_summary(tasks)
            print("\n--- TASK SUMMARY ---")
            print(f"Total Tasks: {total}")
            print(f"Completed Tasks: {completed}")
            print(f"Pending Tasks: {pending}")
            print(f"Completion Rate: {percentage:.2f}%")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
