from sqlalchemy import Column, String, DateTime, Integer, Float
from datetime import datetime
from uuid import uuid4

from app.db.session import Base


class AgentRun(Base):

    __tablename__ = "agent_runs"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))

    job_id = Column(String, nullable=False)

    agent_name = Column(String, nullable=False)

    status = Column(String, nullable=False)

    reasoning = Column(String, nullable=True)

    input_tokens = Column(Integer, default=0)

    output_tokens = Column(Integer, default=0)

    latency_ms = Column(Float, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)