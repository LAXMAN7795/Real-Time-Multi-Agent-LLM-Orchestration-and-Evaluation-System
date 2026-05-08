from datetime import datetime

from app.llm.services.llm_service import (
    LLMService
)

from app.llm.prompts.security_prompt import (
    SECURITY_SYSTEM_PROMPT
)


def security_node(state):

    query = state["user_query"]

    security_analysis = (
        LLMService.generate_response(
            system_prompt=SECURITY_SYSTEM_PROMPT,
            user_prompt=query
        )
    )

    lowered_analysis = security_analysis.lower()

    if "malicious" in lowered_analysis:

        state["security_decision"] = "blocked"

        state["final_response"] = (
            "Request blocked due to "
            "security policy violation."
        )

    elif "suspicious" in lowered_analysis:

        state["security_decision"] = "flagged"

    else:

        state["security_decision"] = "safe"

    state["security_analysis"] = security_analysis

    state["execution_trace"].append({

        "agent": "security_agent",

        "event": "security_analysis_completed",

        "timestamp": datetime.utcnow().isoformat(),

        "decision": state["security_decision"]

    })

    return state