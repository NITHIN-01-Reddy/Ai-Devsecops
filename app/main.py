from fastapi import FastAPI
from app.routes.tasks import router as task_router
from app.logger import logger
import random
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="AI DevSecOps Platform",
    version="1.0.0"
)

app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def home():
    logger.info("Home endpoint accessed")
    return {
        "message": "AI DevSecOps Platform Running"
    }

@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {
        "status": "healthy"
    }

@app.get("/simulate-error")
def simulate_error():
    logger.error("Simulated application error")

    if random.randint(0, 1):  # nosec B311 - intentional failure simulation
        raise Exception("Random simulated failure")

    return {
        "message": "No error occurred"
    }

Instrumentator().instrument(app).expose(app)