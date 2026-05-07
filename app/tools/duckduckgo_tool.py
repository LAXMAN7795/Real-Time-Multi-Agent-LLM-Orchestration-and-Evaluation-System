from duckduckgo_search import DDGS

from app.tools.schemas import ToolResult


def duckduckgo_search_tool(query: str):

    try:

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=3
                )
            )

        if not results:

            return ToolResult(
                tool_name="duckduckgo_search",
                success=False,
                content="No DuckDuckGo results found."
            )

        combined_content = "\n\n".join([
            result["body"]
            for result in results
        ])

        return ToolResult(
            tool_name="duckduckgo_search",
            success=True,
            content=combined_content,
            source=results[0]["href"],
            metadata={
                "results_count": len(results)
            }
        )

    except Exception as error:

        return ToolResult(
            tool_name="duckduckgo_search",
            success=False,
            content=str(error)
        )