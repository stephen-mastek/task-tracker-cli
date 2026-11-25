from tasks import tasks

def list_tasks():
    """List all tasks in the tasks list."""
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            if isinstance(task, dict):
                task_name = task.get("task", task.get("title", task.get("name", str(task))))
                status = task.get("status")
                if status not in ("pending", "done"):
                    is_done = task.get("done", task.get("completed", False))
                    status = "done" if is_done else "pending"
            else:
                task_name = task
                status = "pending"

            print(f"{index}. {task_name} - {status}")