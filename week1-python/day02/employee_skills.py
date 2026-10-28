employees = [
    {"name": "Rahul", "technologies": ["Python", "Java"]},
    {"name": "Priya", "technologies": ["React", "Python"]},
    {"name": "Alex", "technologies": ["Docker"]},
]

unique_technologies = set()

print("--- EMPLOYEE SKILLS ---")
for employee in employees:
    print(f'{employee["name"]}: {", ".join(employee["technologies"])}')
    unique_technologies.update(employee["technologies"])

print(f"\nUnique technologies: {', '.join(sorted(unique_technologies))}")
