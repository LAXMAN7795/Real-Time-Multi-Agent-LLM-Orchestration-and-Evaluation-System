from fastapi import APIRouter

from app.db.session import SessionLocal
from app.db.models.job import Job

router = APIRouter()


@router.get("/test-db")

async def test_db():

    db = SessionLocal()

    new_job = Job(
        user_query="Test query",
        status="completed"
    )

    db.add(new_job)

    db.commit()

    db.refresh(new_job)

    return {
        "job_id": new_job.id,
        "query": new_job.user_query,
        "status": new_job.status
    }