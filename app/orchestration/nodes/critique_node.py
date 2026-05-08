from datetime import datetime


def critique_node(state):
    if state.get("security_decision") == "blocked":

        return state

    critique = {
        "claim": "Renewable adoption increased",
        "confidence_score": 0.91,
        "issue": None
    }

    state["critique_results"].append(critique)

    state["execution_trace"].append({
        "agent": "critique_agent",
        "event": "critique_completed",
        "timestamp": datetime.utcnow().isoformat()
    })

    return state