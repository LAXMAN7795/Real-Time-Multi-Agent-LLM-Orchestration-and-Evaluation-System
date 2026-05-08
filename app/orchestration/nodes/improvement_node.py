from datetime import datetime

from app.llm.services.llm_service import (
    LLMService
)

from app.llm.prompts.improvement_prompt import (
    IMPROVEMENT_SYSTEM_PROMPT
)


def improvement_node(state):
    if state.get("security_decision") == "blocked":

        return state

    evaluation_result = (
        state["evaluation_result"]
    )

    improvement_analysis = (
        LLMService.generate_response(
            system_prompt=
                IMPROVEMENT_SYSTEM_PROMPT,

            user_prompt=evaluation_result
        )
    )

    lowered_eval = (
        evaluation_result.lower()
    )

    if "hallucination risk: high" in lowered_eval:

        state["retry_recommended"] = True

    else:

        state["retry_recommended"] = False

    state["improvement_analysis"] = (
        improvement_analysis
    )

    state["execution_trace"].append({

        "agent": "improvement_agent",

        "event": "self_improvement_completed",

        "timestamp": datetime.utcnow().isoformat(),

        "retry_recommended":
            state["retry_recommended"]

    })

    return state