class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.tasks_completed = 0

    def complete_task(self):
        self.tasks_completed += 1

    def display_summary(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Tasks Completed: {self.tasks_completed}")


first_employee = Employee("Rahul", "Engineering")
second_employee = Employee("Priya", "Design")

first_employee.complete_task()
first_employee.complete_task()
second_employee.complete_task()

first_employee.display_summary()
print()
second_employee.display_summary()
