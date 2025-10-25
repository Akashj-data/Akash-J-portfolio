"""
LangGraph orchestration (optional for the demo). This wires LLM intent with tools.
You can run the Streamlit scripted flow without this; add later for extra credit.
"""
from typing import TypedDict, Literal
from langgraph.graph import StateGraph, END

class BookingState(TypedDict, total=False):
    intent: str
    patient: dict
    preference: dict
    proposed_slots: list
    booking: dict

def node_greet(state: BookingState) -> BookingState:
    return {"intent": "greet"}

def node_lookup(state: BookingState) -> BookingState:
    # TODO: call PatientDB
    return state

def node_plan(state: BookingState) -> BookingState:
    # TODO: 60/30 duration logic + ScheduleDB.find_free_slots
    return state

def build_graph():
    g = StateGraph(BookingState)
    g.add_node("greet", node_greet)
    g.add_node("lookup", node_lookup)
    g.add_node("plan", node_plan)
    g.set_entry_point("greet")
    g.add_edge("greet", "lookup")
    g.add_edge("lookup", "plan")
    g.add_edge("plan", END)
    return g.compile()

def run_graph(user_message: str, state: BookingState | None = None) -> BookingState:
    state = state or {}
    graph = build_graph()
    return graph.invoke(state)
