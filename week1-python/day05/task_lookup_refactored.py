import logging


logger = logging.getLogger(__name__)


def find_task_by_id(tasks: list[dict], task_id: int) -> dict | None:
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def build_task_index(tasks: list[dict]) -> dict[int, dict]:
    index: dict[int, dict] = {}
    for task in tasks:
        task_id = task["id"]
        if task_id in index:
            raise ValueError(f"Duplicate task ID: {task_id}")
        index[task_id] = task
    return index


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    tasks = [
        {"id": 101, "title": "Create PRD", "completed": True},
        {"id": 102, "title": "Design API", "completed": False},
        {"id": 103, "title": "Build Backend", "completed": False},
        {"id": 104, "title": "Write Tests", "completed": False},
    ]
    tasks_by_id = build_task_index(tasks)

    print("--- TASK LOOKUP ---")
    print("\nList Search:")
    list_result = find_task_by_id(tasks, 103)
    if list_result is not None:
        print(f'{list_result["id"]}. {list_result["title"]}')

    print("\nDictionary Search:")
    dictionary_result = tasks_by_id.get(103)
    if dictionary_result is not None:
        print(f'{dictionary_result["id"]}. {dictionary_result["title"]}')

    print("\nSearch for ID 999:")
    missing_id = 999
    missing_task = tasks_by_id.get(missing_id)
    if missing_task is None:
        logger.warning("Task ID %s was not found", missing_id)
        print("Task not found.")


if __name__ == "__main__":
    main()
