import uuid
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class RepoUrl(BaseModel):
    repo_url: str


@router.post("/analyze")
async def analyze_repository(repo_url: RepoUrl):
    task_id = str(uuid.uuid4())
    print(f"Accepted job for {repo_url.repo_url}. Task ID: {task_id}")
    return {"task_id": task_id}


@router.get("/status/{task_id}")
async def get_status(task_id: str):
    print(f"Checking status for: {task_id}")
    return {"status": "Pending"}


@router.get("/result/{task_id}")
async def get_result(task_id: str):
    print(f"Checking result for: {task_id}")
    return {
        "nodes": [
            {"id": "main.py", "lines": 150, "complexity": 10, "heat": 0.9},
            {"id": "utils.py", "lines": 50, "complexity": 2, "heat": 0.2},
        ],
        "links": [
            {"source": "main.py", "target": "utils.py"},
        ]
    }
