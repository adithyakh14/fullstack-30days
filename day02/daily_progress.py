
total_tasks = 20
completed_tasks = 0

for day in range(1, 6):
    print(f"\nDay {day}")

    daily_completed = int(input("Tasks completed today: "))

    remaining_tasks = total_tasks - completed_tasks

    if daily_completed < 0 or daily_completed > remaining_tasks:
        print("Invalid task count. Stopping.")
        break

    completed_tasks += daily_completed

    print(f"Total completed: {completed_tasks}")
    print(f"Remaining tasks: {total_tasks - completed_tasks}")

    if completed_tasks == total_tasks:
        print("All tasks completed!")
        break

print("\n--- FINAL SUMMARY ---")
print(f"Completed: {completed_tasks}")
print(f"Pending: {total_tasks - completed_tasks}")
