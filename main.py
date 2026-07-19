from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Create the FastAPI application
app = FastAPI(
    title="Task API",
    description="A simple CRUD API built with FastAPI for the FlyRank Backend AI Engineering Internship.",
    version="1.0.0"
)


# ==========================
# Pydantic Models
# ==========================

class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str
    done: bool


# ==========================
# In-memory Database
# ==========================

tasks = [
    {
        "id": 1,
        "title": "Study FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Buy Milk",
        "done": True
    },
    {
        "id": 3,
        "title": "Complete FlyRank Assignment",
        "done": False
    }
]


# ==========================
# Root Endpoint
# ==========================

@app.get(
    "/",
    summary="API Information",
    description="Returns basic information about the Task API."
)
def root():
    return {
        "name": "Task API",
        "version": "1.0.0",
        "endpoints": [
            "/health",
            "/tasks"
        ]
    }


# ==========================
# Health Check
# ==========================

@app.get(
    "/health",
    summary="Health Check",
    description="Checks whether the API is running."
)
def health():
    return {
        "status": "ok"
    }


# ==========================
# Get All Tasks
# ==========================

@app.get(
    "/tasks",
    summary="Get All Tasks",
    description="Returns all tasks."
)
def get_tasks():
    return tasks


# ==========================
# Get One Task
# ==========================

@app.get(
    "/tasks/{task_id}",
    summary="Get Task by ID",
    description="Returns a single task by its ID."
)
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )


# ==========================
# Create Task
# ==========================

@app.post(
    "/tasks",
    status_code=status.HTTP_201_CREATED,
    summary="Create Task",
    description="Creates a new task."
)
def create_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title is required"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


# ==========================
# Update Task
# ==========================

@app.put(
    "/tasks/{task_id}",
    summary="Update Task",
    description="Updates an existing task."
)
def update_task(task_id: int, updated_task: TaskUpdate):

    if updated_task.title.strip() == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title is required"
        )

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["done"] = updated_task.done
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )


# ==========================
# Delete Task
# ==========================

@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Task",
    description="Deletes a task."
)
def delete_task(task_id: int):

    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task {task_id} not found"
    )