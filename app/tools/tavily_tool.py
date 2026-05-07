from tavily import TavilyClient

from app.core.config import settings

from app.tools.schemas import ToolResult


client = TavilyClient(
    api_key=settings.TAVILY_API_KEY
)


def tavily_search_tool(query: str):

    try:

        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=3
        )

        results = response.get("results", [])

        if not results:

            return ToolResult(
                tool_name="tavily_search",
                success=False,
                content="No Tavily results found."
            )

        combined_content = "\n\n".join([

            result["content"]

            for result in results

        ])

        return ToolResult(
            tool_name="tavily_search",
            success=True,
            content=combined_content,
            source=results[0]["url"],
            metadata={
                "results_count": len(results)
            }
        )

    except Exception as error:

        return ToolResult(
            tool_name="tavily_search",
            success=False,
            content=str(error)
        )