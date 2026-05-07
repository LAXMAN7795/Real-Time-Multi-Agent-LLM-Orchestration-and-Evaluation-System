from sqlalchemy import Column, String, DateTime, Float, JSON
from datetime import datetime
from uuid import uuid4

from app.db.session import Base


class EvalRun(Base):

    __tablename__ = "eval_runs"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))

    test_case_name = Column(String, nullable=False)

    score = Column(Float, default=0)

    justification = Column(String)

    dimension_scores = Column(JSON)

    created_at = Column(DateTime, default=datetime.utcnow)