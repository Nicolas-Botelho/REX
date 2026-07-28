from langgraph.graph import START, END, StateGraph

from ai_gen.state import State, NoStructState
from ai_gen.agents.domain_narrative_agent import call_llm as call_narrative, call_llm_no_struct as cnns
from ai_gen.agents.requirement_agent import call_llm as call_requirement, call_llm_no_struct as crns
from ai_gen.agents.class_agent import call_llm as call_class, call_llm_no_struct as ccns
from ai_gen.agents.usecase_agent import call_llm as call_usecase, call_llm_no_struct as cuns

# Full Workflow and Graph
full_workflow = StateGraph(State)

full_workflow.add_node("dn_node", call_narrative)
full_workflow.add_node("req_node", call_requirement)
full_workflow.add_node("uc_node", call_usecase)
full_workflow.add_node("cls_node", call_class)

full_workflow.add_edge(START, "dn_node")
full_workflow.add_edge("dn_node", "req_node")
full_workflow.add_edge("req_node", "uc_node")
full_workflow.add_edge("uc_node", "cls_node")
full_workflow.add_edge("cls_node", END)

full_graph = full_workflow.compile()

no_struct_workflow = StateGraph(NoStructState)

no_struct_workflow.add_node("dn_node", cnns)
no_struct_workflow.add_node("req_node", crns)
no_struct_workflow.add_node("uc_node", cuns)
no_struct_workflow.add_node("cls_node", ccns)

no_struct_workflow.add_edge(START, "dn_node")
no_struct_workflow.add_edge("dn_node", "req_node")
no_struct_workflow.add_edge("req_node", "uc_node")
no_struct_workflow.add_edge("uc_node", "cls_node")
no_struct_workflow.add_edge("cls_node", END)

ns_graph = no_struct_workflow.compile()