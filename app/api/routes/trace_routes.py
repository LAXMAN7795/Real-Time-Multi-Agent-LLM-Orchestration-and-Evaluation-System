from fastapi import APIRouter, HTTPException

from app.core.job_store import JOB_STORE


router = APIRouter()


@router.get("/trace/{job_id}")

async def get_trace(job_id: str):

    if job_id not in JOB_STORE:

        raise HTTPException(

            status_code=404,

            detail={

                "error_code": "TRACE_NOT_FOUND",

                "message": "Job trace not found.",

                "job_id": job_id

            }

        )

    return JOB_STORE[job_id]