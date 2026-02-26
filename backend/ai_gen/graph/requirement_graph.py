from langgraph.graph import START, END, StateGraph

from backend.ai_gen.state import State
from backend.ai_gen.agents.br_agent import call_llm as call_br
from backend.ai_gen.agents.fr_agent import call_llm as call_fr
from backend.ai_gen.agents.nfr_agent import call_llm as call_nfr

workflow = StateGraph(State)

workflow.add_node("fr_node", call_fr)
workflow.add_node("nfr_node", call_nfr)
workflow.add_node("br_node", call_br)

workflow.add_edge(START, "fr_node")
workflow.add_edge("fr_node", "nfr_node")
workflow.add_edge("nfr_node", "br_node")
workflow.add_edge("br_node", END)

graph = workflow.compile()