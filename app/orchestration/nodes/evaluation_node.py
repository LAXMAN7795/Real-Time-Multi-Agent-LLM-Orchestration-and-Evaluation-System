from datetime import datetime

from app.llm.services.llm_service import (
    LLMService
)

from app.llm.prompts.evaluation_prompt import (
    EVALUATION_SYSTEM_PROMPT
)


def evaluation_node(state):

    retrieved_chunks = state["retrieved_chunks"]

    synthesized_response = state["final_response"]

    evidence_text = "\n\n".join([

        chunk["content"]

        for chunk in retrieved_chunks

    ])

    evaluation_prompt = f"""
User Query:
{state['user_query']}

Retrieved Evidence:
{evidence_text}

Generated Response:
{synthesized_response}

Evaluate the generated response.
"""

    evaluation_result = (
        LLMService.generate_response(
            system_prompt=EVALUATION_SYSTEM_PROMPT,
            user_prompt=evaluation_prompt
        )
    )

    state["evaluation_result"] = evaluation_result

    state["messages"].append({
        "agent": "evaluation_agent",
        "output": evaluation_result
    })

    state["execution_trace"].append({
        "agent": "evaluation_agent",
        "event": "response_evaluated",
        "timestamp": datetime.utcnow().isoformat()
    })

    return state