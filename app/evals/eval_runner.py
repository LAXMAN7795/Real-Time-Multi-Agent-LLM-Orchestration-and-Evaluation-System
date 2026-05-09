from datetime import datetime

from app.orchestration.graph import graph

from app.evals.test_cases import TEST_CASES
from app.core.eval_store import (
    FAILED_EVAL_CASES
)


def run_evaluation_suite():

    results = []

    for test_case in TEST_CASES:

        initial_state = {

            "job_id": test_case["id"],

            "user_query": test_case["query"],

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
            "is_eval_mode": True,
            "evaluation_metrics": {}

        }

        result = graph.invoke(initial_state)
        evaluation_result = (
            result["evaluation_result"]
        )

        lowered_eval = (
            evaluation_result.lower()
        )

        failed = False

        if (
            "hallucination risk: high"
            in lowered_eval
        ):

            failed = True

        if (
            "groundedness_score"
            in lowered_eval
        ):

            if "0.5" in lowered_eval:

                failed = True

        results.append({

            "test_case_id": test_case["id"],

            "category": test_case["category"],

            "query": test_case["query"],

            "final_response": result["final_response"],

            "evaluation_result": result["evaluation_result"],

            "timestamp": datetime.utcnow().isoformat()

        })
        if failed:

            FAILED_EVAL_CASES[
                test_case["id"]
            ] = {

                "test_case": test_case,

                "evaluation_result":
                    evaluation_result,

                "timestamp":
                    datetime.utcnow().isoformat()

            }

    return results