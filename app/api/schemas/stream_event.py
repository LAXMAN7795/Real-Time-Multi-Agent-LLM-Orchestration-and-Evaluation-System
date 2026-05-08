from pydantic import BaseModel


class StreamEvent(BaseModel):

    agent: str

    event: str

    message: str