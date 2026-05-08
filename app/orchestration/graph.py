from langgraph.graph import StateGraph, END

from app.orchestration.state import OrchestratorState

from app.orchestration.nodes.decomposition_node import decomposition_node
from app.orchestration.nodes.retrieval_node import retrieval_node
from app.orchestration.nodes.critique_node import critique_node
from app.orchestration.nodes.synthesis_node import synthesis_node
from app.orchestration.nodes.evaluation_node import evaluation_node

from app.orchestration.router import dynamic_router
from app.orchestration.nodes.security_node import (
    security_node
)
from app.orchestration.nodes.improvement_node import (
    improvement_node
)


workflow = StateGraph(OrchestratorState)

workflow.add_node("decomposition", decomposition_node)
workflow.add_node("retrieval", retrieval_node)
workflow.add_node("critique", critique_node)
workflow.add_node("synthesis", synthesis_node)
workflow.add_node("evaluation", evaluation_node)
workflow.add_node("security", security_node)
workflow.add_node("improvement",improvement_node)


workflow.set_conditional_entry_point(
    dynamic_router,
    {
        "decomposition": "decomposition",
        "retrieval": "retrieval"
    }
)

workflow.add_edge("decomposition", "retrieval")

workflow.add_edge("retrieval", "security")

workflow.add_edge("security", "critique")

workflow.add_edge("critique", "synthesis")

workflow.add_edge("synthesis", "evaluation")

workflow.add_edge("evaluation","improvement")

workflow.add_edge("improvement",END)

graph = workflow.compile()