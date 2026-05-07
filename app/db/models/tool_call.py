from sqlalchemy import Column, String, DateTime, Float, JSON, Boolean
from datetime import datetime
from uuid import uuid4

from app.db.session import Base


class ToolCall(Base):

    __tablename__ = "tool_calls"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))

    job_id = Column(String, nullable=False)

    tool_name = Column(String, nullable=False)

    input_data = Column(JSON)

    output_data = Column(JSON)

    latency_ms = Column(Float, default=0)

    success = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)