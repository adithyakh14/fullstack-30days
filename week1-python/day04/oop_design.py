
class Employee:
    def __init__(self, name):
        self.name = name
        self._tasks_completed = 0

    @property
    def tasks_completed(self):
        return self._tasks_completed

    def complete_task(self):
        self._tasks_completed += 1


class Manager(Employee):
    def __init__(self, name, team_name):
        super().__init__(name)
        self.team_name = team_name


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, employee):
        self.members.append(employee)

    def total_completed_tasks(self):
        total = 0

        for member in self.members:
            total += member.tasks_completed

        return total


rahul = Employee("Rahul")
priya = Manager("Priya", "Backend Team")

rahul.complete_task()
rahul.complete_task()
priya.complete_task()

team = Team("Engineering")
team.add_member(rahul)
team.add_member(priya)

print(f"Team: {team.name}")
print(f"Members: {len(team.members)}")
print(f"Completed Tasks: {team.total_completed_tasks()}")
