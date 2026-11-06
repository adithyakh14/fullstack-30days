
class Task:
    def __init__(self, task_id, title, priority):
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        if self.completed:
            return False

        self.completed = True
        return True

    def display(self):
        status = "Completed" if self.completed else "Pending"
        print(f"{self.task_id}. {self.title} | {self.priority} | {status}")


task1 = Task(1, "Create PRD", "High")
task2 = Task(2, "Design Dashboard", "Medium")

print("--- BEFORE ---")
task1.display()
task2.display()

task1.mark_completed()

print("\n--- AFTER ---")
task1.display()
task2.display()
