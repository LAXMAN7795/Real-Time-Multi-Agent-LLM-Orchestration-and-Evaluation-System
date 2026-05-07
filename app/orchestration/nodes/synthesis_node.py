from datetime import datetime


def synthesis_node(state):

    response = (
        "India has significantly increased "
        "renewable energy investments."
    )

    state["final_response"] = response

    state["execution_trace"].append({
        "agent": "synthesis_agent",
        "event": "response_generated",
        "timestamp": datetime.utcnow().isoformat()
    })

    return state