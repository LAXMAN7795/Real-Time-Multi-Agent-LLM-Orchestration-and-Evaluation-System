from app.tools.schemas import ToolResult


MOCK_KNOWLEDGE = {

    "quantum computing":
        (
            "Quantum computing is a type "
            "of computation that uses "
            "quantum mechanics principles "
            "such as superposition and "
            "entanglement."
        ),

    "artificial intelligence":
        (
            "Artificial intelligence "
            "enables machines to simulate "
            "human intelligence."
        )
}


def mock_search_tool(query: str):

    normalized_query = query.lower()

    for key in MOCK_KNOWLEDGE:

        if key in normalized_query:

            return ToolResult(
                tool_name="mock_search",
                success=True,
                content=MOCK_KNOWLEDGE[key],
                source="mock_provider"
            )

    return ToolResult(
        tool_name="mock_search",
        success=False,
        content="No mock retrieval result found."
    )