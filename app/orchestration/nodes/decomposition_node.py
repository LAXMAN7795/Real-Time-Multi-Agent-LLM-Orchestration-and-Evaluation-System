from datetime import datetime

from app.llm.services.llm_service import LLMService

from app.llm.prompts.decomposition_prompt import (
    DECOMPOSITION_SYSTEM_PROMPT
)


def decomposition_node(state):

    query = state["user_query"]

    decomposition_output = LLMService.generate_response(
        system_prompt=DECOMPOSITION_SYSTEM_PROMPT,
        user_prompt=query
    )

    state["messages"].append({
        "agent": "decomposition_agent",
        "output": decomposition_output
    })

    state["execution_trace"].append({
        "agent": "decomposition_agent",
        "event": "query_decomposed",
        "timestamp": datetime.utcnow().isoformat()
    })

    return state