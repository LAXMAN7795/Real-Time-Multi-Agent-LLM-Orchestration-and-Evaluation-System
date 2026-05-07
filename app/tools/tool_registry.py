from app.tools.wikipedia_tool import (
    wikipedia_search_tool
)

from app.tools.duckduckgo_tool import (
    duckduckgo_search_tool
)
from app.tools.mock_search_tool import (
    mock_search_tool
)


TOOLS = {

    "wikipedia_search": wikipedia_search_tool,

    "duckduckgo_search": duckduckgo_search_tool,

    "mock_search": mock_search_tool

}