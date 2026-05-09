from fastapi import APIRouter

from app.orchestration.graph import graph

from app.core.eval_store import (
    FAILED_EVAL_CASES
)


router = APIRouter()


@router.get("/rerun-failed-evals")

async def rerun_failed_evals():

    rerun_results = []

    for case_id, case_data in (
        FAILED_EVAL_CASES.items()
    ):

        test_case = (
            case_data["test_case"]
        )

        initial_state = {

            "job_id": test_case["id"],

            "user_query":
                test_case["query"],

            "current_agent": "",

            "messages": [],

            "retrieved_chunks": [],

            "critique_results": [],

            "execution_trace": [],

            "final_response": "",

            "provenance": [],

            "evaluation_result": "",

            "security_analysis": "",

            "security_decision": "",

            "context_budget": {},

            "improvement_analysis": "",

            "retry_recommended": False,

            "rewrite_id": "",

            "evaluation_metrics": {}

        }

        result = graph.invoke(
            initial_state
        )

        rerun_results.append({

            "test_case_id": case_id,

            "query":
                test_case["query"],

            "new_evaluation":
                result["evaluation_result"],

            "new_response":
                result["final_response"]

        })

    return rerun_results