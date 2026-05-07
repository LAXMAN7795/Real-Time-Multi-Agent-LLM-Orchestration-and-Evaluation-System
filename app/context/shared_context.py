from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class ToolCallLog(BaseModel):

    tool_name: str

    input_data: Dict[str, Any]

    output_data: Dict[str, Any]

    latency_ms: float

    success: bool

    retry_count: int = 0


class AgentExecution(BaseModel):

    agent_name: str

    started_at: datetime

    completed_at: Optional[datetime] = None

    input_tokens: int = 0

    output_tokens: int = 0

    status: str

    reasoning: Optional[str] = None

    policy_violations: List[str] = Field(default_factory=list)


class CritiqueResult(BaseModel):

    claim: str

    confidence_score: float

    issue: Optional[str] = None

    flagged_span: Optional[str] = None


class ProvenanceRecord(BaseModel):

    sentence: str

    source_agent: str

    source_chunk_id: Optional[str] = None


class SharedContext(BaseModel):

    job_id: str

    user_query: str

    current_agent: Optional[str] = None

    messages: List[Dict[str, Any]] = Field(default_factory=list)

    retrieved_chunks: List[Dict[str, Any]] = Field(default_factory=list)

    tool_calls: List[ToolCallLog] = Field(default_factory=list)

    agent_executions: List[AgentExecution] = Field(default_factory=list)

    critique_results: List[CritiqueResult] = Field(default_factory=list)

    provenance_records: List[ProvenanceRecord] = Field(default_factory=list)

    execution_trace: List[Dict[str, Any]] = Field(default_factory=list)

    shared_memory: Dict[str, Any] = Field(default_factory=dict)

    metadata: Dict[str, Any] = Field(default_factory=dict)