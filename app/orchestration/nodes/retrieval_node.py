from datetime import datetime

from app.rag.retriever import retrieve_documents

from app.tools.wikipedia_tool import (
    wikipedia_search_tool
)

from app.tools.duckduckgo_tool import (
    duckduckgo_search_tool
)
from app.tools.mock_search_tool import (
    mock_search_tool
)


SIMILARITY_THRESHOLD = 0.7


def retrieval_node(state):

    query = state["user_query"]

    rag_chunks = retrieve_documents(query)

    relevant_rag_chunks = []

    for chunk in rag_chunks:

        if chunk["distance"] < SIMILARITY_THRESHOLD:

            relevant_rag_chunks.append(chunk)

    retrieved_chunks = relevant_rag_chunks.copy()

    external_tools_used = []

    if len(relevant_rag_chunks) == 0:

        wiki_result = wikipedia_search_tool(query)

        state["execution_trace"].append({
            "agent": "retrieval_agent",
            "event": "wikipedia_tool_result",
            "tool_success": wiki_result.success,
            "tool_output": wiki_result.content
        })

        external_tools_used.append(
            "wikipedia_search"
        )

        if wiki_result.success:

            retrieved_chunks.append({
                "chunk_id": "wikipedia_result",
                "content": wiki_result.content,
                "source": wiki_result.source
            })

        else:

            ddg_result = duckduckgo_search_tool(query)

            state["execution_trace"].append({
                "agent": "retrieval_agent",
                "event": "duckduckgo_tool_result",
                "tool_success": ddg_result.success,
                "tool_output": ddg_result.content
            })

            external_tools_used.append(
                "duckduckgo_search"
            )

            if ddg_result.success:

                retrieved_chunks.append({
                    "chunk_id": "duckduckgo_result",
                    "content": ddg_result.content,
                    "source": ddg_result.source
                })

            else:

                mock_result = mock_search_tool(query)

                state["execution_trace"].append({
                    "agent": "retrieval_agent",
                    "event": "mock_tool_result",
                    "tool_success": mock_result.success,
                    "tool_output": mock_result.content
                })

                external_tools_used.append(
                    "mock_search"
                )

                if mock_result.success:

                    retrieved_chunks.append({
                        "chunk_id": "mock_result",
                        "content": mock_result.content,
                        "source": mock_result.source
                    })

    state["retrieved_chunks"] = retrieved_chunks

    state["execution_trace"].append({
        "agent": "retrieval_agent",
        "event": "adaptive_retrieval_completed",
        "timestamp": datetime.utcnow().isoformat(),
        "chunks_count": len(retrieved_chunks),
        "external_tools_used": external_tools_used
    })

    return state