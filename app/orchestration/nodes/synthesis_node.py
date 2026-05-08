from datetime import datetime

from app.llm.services.llm_service import (
    LLMService
)

from app.llm.prompts.synthesis_prompt import (
    SYNTHESIS_SYSTEM_PROMPT
)


def synthesis_node(state):
    if state.get("security_decision") == "blocked":

        return state

    retrieved_chunks = state["retrieved_chunks"]

    if not retrieved_chunks:

        state["final_response"] = (
            "No sufficient evidence retrieved."
        )

        return state

    evidence_text = "\n\n".join([

        (
            f"Source: {chunk.get('source', 'unknown')}\n"
            f"Content: {chunk['content']}"
        )

        for chunk in retrieved_chunks

    ])

    user_prompt = f"""
User Query:
{state['user_query']}

Retrieved Evidence:
{evidence_text}

Generate a grounded response using only
the retrieved evidence.
"""

    synthesized_response = (
        LLMService.generate_response(
            system_prompt=SYNTHESIS_SYSTEM_PROMPT,
            user_prompt=user_prompt
        )
    )

    provenance = [

        {
            "source": chunk.get("source"),
            "chunk_id": chunk.get("chunk_id")
        }

        for chunk in retrieved_chunks

    ]

    state["final_response"] = synthesized_response

    state["messages"].append({
        "agent": "synthesis_agent",
        "output": synthesized_response
    })

    state["execution_trace"].append({
        "agent": "synthesis_agent",
        "event": "grounded_synthesis_completed",
        "timestamp": datetime.utcnow().isoformat(),
        "sources_used": provenance
    })

    state["provenance"] = provenance

    return state