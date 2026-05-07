from datetime import datetime


def decomposition_node(state):

    query = state["user_query"]

    subtasks = [
        {
            "task": f"Analyze query: {query}",
            "depends_on": []
        }
    ]

    state["execution_trace"].append({
        "agent": "decomposition_agent",
        "event": "query_decomposed",
        "timestamp": datetime.utcnow().isoformat(),
        "subtasks": subtasks
    })

    state["messages"].append({
        "agent": "decomposition_agent",
        "output": subtasks
    })

    return state