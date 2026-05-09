from fastapi import APIRouter

from app.evals.test_cases import (
    TEST_CASES
)

from app.core.eval_store import (
    FAILED_EVAL_CASES
)


router = APIRouter()


@router.get("/eval-summary")

async def get_eval_summary():

    total_cases = len(TEST_CASES)

    failed_cases = len(
        FAILED_EVAL_CASES
    )

    passed_cases = (
        total_cases - failed_cases
    )

    hallucination_failures = 0

    security_blocks = 0

    for _, case_data in (
        FAILED_EVAL_CASES.items()
    ):

        evaluation_result = (
            case_data["evaluation_result"]
        ).lower()

        if (
            "hallucination risk: high"
            in evaluation_result
        ):

            hallucination_failures += 1

        if (
            "blocked"
            in evaluation_result
        ):

            security_blocks += 1

    pass_rate = round(

        (passed_cases / total_cases) * 100,

        2

    )

    return {

        "total_cases": total_cases,

        "passed_cases": passed_cases,

        "failed_cases": failed_cases,

        "pass_rate_percentage":
            pass_rate,

        "hallucination_failures":
            hallucination_failures,

        "security_blocks":
            security_blocks

    }