from fastapi import APIRouter
from uuid import uuid4

from app.context.shared_context import SharedContext

router = APIRouter()


@router.get("/test-context")
async def test_context():

    context = SharedContext(
        job_id=str(uuid4()),
        user_query="Explain renewable energy adoption"
    )

    return context.model_dump()