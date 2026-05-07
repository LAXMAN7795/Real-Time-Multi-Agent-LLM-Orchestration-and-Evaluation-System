from app.tools.wikipedia_tool import (
    wikipedia_search_tool
)

from app.tools.mock_search_tool import (
    mock_search_tool
)

from app.tools.tavily_tool import (
    tavily_search_tool
)


TOOLS = {

    "wikipedia_search": wikipedia_search_tool,

    "tavily_search": tavily_search_tool,

    "mock_search": mock_search_tool,


}