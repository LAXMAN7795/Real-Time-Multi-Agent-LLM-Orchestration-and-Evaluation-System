from fastapi import APIRouter
from uuid import uuid4

from app.orchestration.graph import graph
from app.core.job_store import JOB_STORE


router = APIRouter()


@router.post("/run-orchestrator")

async def run_orchestrator(payload: dict):

    state = {
        "job_id": str(uuid4()),
        "user_query": payload["query"],
        "current_agent": "",
        "messages": [],
        "retrieved_chunks": [],
        "critique_results": [],
        "execution_trace": [],
        "final_response": "",
        "provenance": [],
        "evaluation_result": ""
    }

    result = graph.invoke(state)

    JOB_STORE[result["job_id"]] = result

    return result