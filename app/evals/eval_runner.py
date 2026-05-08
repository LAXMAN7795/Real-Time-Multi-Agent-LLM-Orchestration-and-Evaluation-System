from datetime import datetime

from app.orchestration.graph import graph

from app.evals.test_cases import TEST_CASES


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

            "security_decision": ""

        }

        result = graph.invoke(initial_state)

        results.append({

            "test_case_id": test_case["id"],

            "category": test_case["category"],

            "query": test_case["query"],

            "final_response": result["final_response"],

            "evaluation_result": result["evaluation_result"],

            "timestamp": datetime.utcnow().isoformat()

        })

    return results