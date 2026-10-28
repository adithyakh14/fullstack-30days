
from pathlib import Path

file_path = Path(__file__).with_name("task_notes.txt")

# Step 1: Save initial tasks
with file_path.open("w", encoding="utf-8") as file:
    file.write("Create PRD\n")
    file.write("Prepare Design\n")

# Step 2: Append another task
with file_path.open("a", encoding="utf-8") as file:
    file.write("Plan Implementation\n")

# Step 3: Read saved tasks
with file_path.open("r", encoding="utf-8") as file:
    print("--- SAVED TASKS ---")

    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}")
