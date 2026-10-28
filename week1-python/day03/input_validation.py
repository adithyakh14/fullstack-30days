def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                raise ValueError("Number must be positive.")

        except ValueError as error:
            print(f"Invalid input: {error}")

        else:
            return value


task_id = read_positive_integer("Enter a task ID: ")

print(f"Valid task ID: {task_id}")
