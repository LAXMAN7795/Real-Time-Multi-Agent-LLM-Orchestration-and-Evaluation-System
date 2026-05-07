from typing import TypedDict, List, Dict, Any


class OrchestratorState(TypedDict):

    job_id: str

    user_query: str

    current_agent: str

    messages: List[Dict[str, Any]]

    retrieved_chunks: List[Dict[str, Any]]

    critique_results: List[Dict[str, Any]]

    execution_trace: List[Dict[str, Any]]

    final_response: str