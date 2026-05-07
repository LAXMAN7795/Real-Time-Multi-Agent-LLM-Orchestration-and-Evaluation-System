from langgraph.graph import StateGraph, END

from app.orchestration.state import OrchestratorState

from app.orchestration.nodes.decomposition_node import decomposition_node
from app.orchestration.nodes.retrieval_node import retrieval_node
from app.orchestration.nodes.critique_node import critique_node
from app.orchestration.nodes.synthesis_node import synthesis_node

from app.orchestration.router import dynamic_router


workflow = StateGraph(OrchestratorState)

workflow.add_node("decomposition", decomposition_node)
workflow.add_node("retrieval", retrieval_node)
workflow.add_node("critique", critique_node)
workflow.add_node("synthesis", synthesis_node)


workflow.set_conditional_entry_point(
    dynamic_router,
    {
        "decomposition": "decomposition",
        "retrieval": "retrieval"
    }
)

workflow.add_edge("decomposition", "retrieval")

workflow.add_edge("retrieval", "critique")

workflow.add_edge("critique", "synthesis")

workflow.add_edge("synthesis", END)

graph = workflow.compile()