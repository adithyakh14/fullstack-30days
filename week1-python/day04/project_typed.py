class Task:
    def __init__(self, task_id: int, title: str, priority: str) -> None:
        self.task_id = task_id
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_completed(self) -> None:
        self.completed = True

    def display(self) -> None:
        status = "Completed" if self.completed else "Pending"
        print(f"{self.task_id}. {self.title} | {self.priority} | {status}")


class Project:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def display_tasks(self) -> None:
        print(f"Project: {self.name}")
        if not self.tasks:
            print("No tasks yet.")
        for task in self.tasks:
            task.display()

    def calculate_completion_rate(self) -> float:
        if not self.tasks:
            return 0.0

        completed_count = 0
        for task in self.tasks:
            if task.completed:
                completed_count += 1
        return completed_count / len(self.tasks) * 100


if __name__ == "__main__":
    project = Project("Website Launch")
    first_task = Task(1, "Create PRD", "High")
    second_task = Task(2, "Design Dashboard", "Medium")
    third_task = Task(3, "Test Database", "High")

    project.add_task(first_task)
    project.add_task(second_task)
    project.add_task(third_task)
    first_task.mark_completed()

    project.display_tasks()
    print(f"Completion Rate: {project.calculate_completion_rate():.2f}%")
