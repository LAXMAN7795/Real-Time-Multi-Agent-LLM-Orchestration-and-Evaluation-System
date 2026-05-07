from datetime import datetime


def retrieval_node(state):

    retrieved_chunks = [
        {
            "chunk_id": "chunk_1",
            "content": "Renewable energy includes solar and wind power."
        },
        {
            "chunk_id": "chunk_2",
            "content": "India increased renewable investments significantly."
        }
    ]

    state["retrieved_chunks"] = retrieved_chunks

    state["execution_trace"].append({
        "agent": "retrieval_agent",
        "event": "chunks_retrieved",
        "timestamp": datetime.utcnow().isoformat(),
        "chunks_count": len(retrieved_chunks)
    })

    return state