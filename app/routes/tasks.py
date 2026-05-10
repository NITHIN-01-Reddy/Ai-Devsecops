from fastapi import APIRouter
from app.logger import logger

router = APIRouter()

tasks = []

@router.get("/")
def get_tasks():
    logger.info("Fetching all tasks")
    return tasks

@router.post("/")
def create_task(task: dict):
    logger.info(f"Creating task: {task}")
    tasks.append(task)
    return {
        "message": "Task created successfully",
        "task": task
    }