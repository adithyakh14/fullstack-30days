from pathlib import Path


file_path = Path(__file__).with_name("saved_tasks.txt")

task_title = input("Enter a task title: ").strip()

with file_path.open("a", encoding="utf-8") as file:
    file.write(f"{task_title}\n")

print("\n--- SAVED TASKS ---")
with file_path.open("r", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")
