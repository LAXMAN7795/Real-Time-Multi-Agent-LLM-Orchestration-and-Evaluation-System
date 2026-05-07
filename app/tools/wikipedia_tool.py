import requests

from app.tools.schemas import ToolResult


WIKIPEDIA_API_URL = (
    "https://en.wikipedia.org/api/rest_v1/page/summary/"
)


def wikipedia_search_tool(query: str):

    try:

        formatted_query = query.replace(
            " ",
            "_"
        )

        response = requests.get(
            WIKIPEDIA_API_URL + formatted_query,
            timeout=10
        )

        if response.status_code != 200:

            return ToolResult(
                tool_name="wikipedia_search",
                success=False,
                content=(
                    f"Wikipedia API returned "
                    f"{response.status_code}"
                )
            )

        data = response.json()

        summary = data.get("extract")

        if not summary:

            return ToolResult(
                tool_name="wikipedia_search",
                success=False,
                content="No summary found."
            )

        return ToolResult(
            tool_name="wikipedia_search",
            success=True,
            content=summary,
            source=data.get("content_urls", {})
                .get("desktop", {})
                .get("page"),
            metadata={
                "title": data.get("title")
            }
        )

    except Exception as error:

        return ToolResult(
            tool_name="wikipedia_search",
            success=False,
            content=str(error)
        )