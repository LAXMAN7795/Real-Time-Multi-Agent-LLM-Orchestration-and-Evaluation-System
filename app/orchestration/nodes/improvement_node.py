from datetime import datetime

from app.llm.services.llm_service import (
    LLMService
)

from app.llm.prompts.improvement_prompt import (
    IMPROVEMENT_SYSTEM_PROMPT
)
import uuid

from app.core.prompt_store import (
    PROMPT_REWRITE_STORE
)


def improvement_node(state):
    if state.get("is_eval_mode"):

        return state
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
    rewrite_id = str(uuid.uuid4())

    PROMPT_REWRITE_STORE[rewrite_id] = {

        "rewrite_id": rewrite_id,

        "job_id": state["job_id"],

        "original_evaluation":
            evaluation_result,

        "proposed_rewrite":
            improvement_analysis,

        "status": "pending",

        "timestamp":
            datetime.utcnow().isoformat()

    }

    state["rewrite_id"] = rewrite_id

    state["execution_trace"].append({

        "agent": "improvement_agent",

        "event": "self_improvement_completed",

        "timestamp": datetime.utcnow().isoformat(),

        "retry_recommended":
            state["retry_recommended"]

    })

    return state