import asyncio
import json
import uuid

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.orchestration.graph import graph


router = APIRouter()


async def event_generator(query: str):

    job_id = str(uuid.uuid4())

    initial_state = {

        "job_id": job_id,

        "user_query": query,

        "current_agent": "",

        "messages": [],

        "retrieved_chunks": [],

        "critique_results": [],

        "execution_trace": [],

        "final_response": "",

        "provenance": [],

        "evaluation_result": ""

    }

    start_event = {

        "agent": "system",

        "event": "job_started",

        "message": f"Job {job_id} started"

    }

    yield f"data: {json.dumps(start_event)}\n\n"

    await asyncio.sleep(0.2)

    result = graph.invoke(initial_state)

    for trace in result["execution_trace"]:

        trace_event = {

            "agent": trace.get("agent"),

            "event": trace.get("event"),

            "message": str(trace)

        }

        yield f"data: {json.dumps(trace_event)}\n\n"

        await asyncio.sleep(0.2)

    final_response_event = {

        "agent": "synthesis_agent",

        "event": "final_response",

        "message": result["final_response"]

    }

    yield f"data: {json.dumps(final_response_event)}\n\n"

    evaluation_event = {

        "agent": "evaluation_agent",

        "event": "evaluation_result",

        "message": result["evaluation_result"]

    }

    yield f"data: {json.dumps(evaluation_event)}\n\n"

    yield "data: [DONE]\n\n"


@router.get("/stream-query")

async def stream_query(query: str):

    return StreamingResponse(

        event_generator(query),

        media_type="text/event-stream"

    )