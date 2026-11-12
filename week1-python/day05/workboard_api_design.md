# WorkBoard API design

Task records have `id`, `title`, `priority`, and `completed`. The server assigns the ID and starts new tasks with `completed: false`.

| User action | Method and endpoint | Request JSON | Success | Missing task | WorkBoard mapping |
| --- | --- | --- | --- | --- | --- |
| View all tasks | `GET /tasks` | None | `200 OK`, with a task list (`[]` when empty) | N/A | Load the task list with `load_tasks()` and return it. |
| View one task | `GET /tasks/{task_id}` | None | `200 OK`, with the task | `404 Not Found` | Add a lookup function, or reuse `find_task_by_id()` from the Day 5 lookup exercise. |
| Create a task | `POST /tasks` | `{"title": "Create PRD", "priority": "High"}` | `201 Created`, with the new task and a `Location` header | N/A | Validate the inputs, call `add_task()`, then `save_tasks()`. |
| Complete a task | `PATCH /tasks/{task_id}` | `{"completed": true}` | `200 OK`, with the updated task | `404 Not Found` | Call `complete_task()`, then `save_tasks()` if it changed the task. An already completed task returns `200 OK` with its unchanged record. |
| Delete a task | `DELETE /tasks/{task_id}` | None | `204 No Content` | `404 Not Found` | Add `delete_task(tasks, task_id)`, then `save_tasks()` after removal. |

Creation requires a nonblank title and a priority of `High`, `Medium`, or `Low`; invalid request data returns `422 Unprocessable Content`. `GET` requests do not change or save tasks. The API loads saved tasks on startup and saves after successful changes.

The method and status choices follow [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110.html); `PATCH` is defined for partial updates in [RFC 5789](https://www.rfc-editor.org/rfc/rfc5789.html).
