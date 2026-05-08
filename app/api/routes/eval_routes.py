from fastapi import APIRouter

from app.evals.eval_runner import (
    run_evaluation_suite
)


router = APIRouter()


@router.get("/run-evals")

async def run_evals():

    return run_evaluation_suite()