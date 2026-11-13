import logging

from fastapi import Body, FastAPI, HTTPException, status


logger = logging.getLogger(__name__)

app = FastAPI(
    title="WorkBoard API",
    description="A task management backend built with FastAPI",
    version="0.1.0",
)

tasks = [
    {"id": 1, "title": "Create PRD", "priority": "High", "completed": True},
    {"id": 2, "title": "Develop API", "priority": "Medium", "completed": False},
]


@app.get("/", tags=["System"])
def home():
    return {"message": "Welcome to WorkBoard API"}


@app.get("/health", tags=["System"])
def health_check():
    return {"status": "healthy"}


@app.get("/tasks", tags=["Tasks"], summary="Retrieve and filter tasks")
def get_tasks(priority: str | None = None, completed: bool | None = None):
    matching_tasks = []
    for task in tasks:
        if priority is not None and task["priority"] != priority:
            continue
        if completed is not None and task["completed"] != completed:
            continue
        matching_tasks.append(task)
    return matching_tasks


@app.get(
    "/tasks/{task_id}",
    tags=["Tasks"],
    summary="Retrieve a task by ID",
    responses={404: {"description": "Task not found"}},
)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    logger.warning("Task ID %s was not found", task_id)
    raise HTTPException(status_code=404, detail="Task not found")


@app.post(
    "/tasks",
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"],
    summary="Create a task",
    responses={422: {"description": "Invalid task data"}},
)
def create_task(payload: dict = Body(...)):
    title = payload.get("title")
    priority = payload.get("priority")

    if not isinstance(title, str) or not title.strip():
        raise HTTPException(status_code=422, detail="Title must be a nonblank string")
    if not isinstance(priority, str) or priority not in {"High", "Medium", "Low"}:
        raise HTTPException(status_code=422, detail="Priority must be High, Medium, or Low")

    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": new_id,
        "title": title.strip(),
        "priority": priority,
        "completed": False,
    }
    tasks.append(new_task)
    return new_task


@app.patch(
    "/tasks/{task_id}",
    tags=["Tasks"],
    summary="Mark a task as completed",
    responses={404: {"description": "Task not found"}},
)
def complete_task(task_id: int, payload: dict = Body(...)):
    if len(payload) != 1 or payload.get("completed") is not True:
        raise HTTPException(status_code=422, detail='Only {"completed": true} is accepted')

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Tasks"],
    summary="Delete a task",
    responses={404: {"description": "Task not found"}},
)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            return None

    raise HTTPException(status_code=404, detail="Task not found")
