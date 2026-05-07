from pydantic import BaseModel
from typing import Optional


class ToolResult(BaseModel):

    tool_name: str

    success: bool

    content: str

    source: Optional[str] = None

    metadata: dict = {}