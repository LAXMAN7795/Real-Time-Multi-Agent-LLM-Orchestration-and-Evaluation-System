from sqlalchemy import Column, String, DateTime, JSON
from datetime import datetime
from uuid import uuid4

from app.db.session import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))

    user_query = Column(String, nullable=False)

    status = Column(String, default="pending")

    final_response = Column(String, nullable=True)

    metadata_json = Column(JSON, default={})

    created_at = Column(DateTime, default=datetime.utcnow)