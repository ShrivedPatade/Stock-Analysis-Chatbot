from typing import TypedDict, List
import pandas as pd
from langgraph.graph import StateGraph
from data_loader import fetch_stock_data
from indicators import apply_indicators
from engine import generate_signals
from visualizer import plot_prediction

def safe_analyze(state):
    if state["data"].empty:
        return state
    # Only apply indicators if data exists
    return {**state, "data": apply_indicators(state["data"])}

def safe_predict(state):
    if state["data"].empty:
        return {**state, "signals": [], "recommendation": "Service Unavailable"}
    return generate_signals(state)

# Define the structured state for the graph
class StockState(TypedDict):
    ticker: str
    period: str
    data: pd.DataFrame
    signals: List[dict]
    recommendation: str

def create_workflow():
    # Initialize the graph with our state definition
    workflow = StateGraph(StockState)

    # Add processing nodes
    workflow.add_node("fetch_data", fetch_stock_data)
    workflow.add_node("analyze_indicators", safe_analyze)
    workflow.add_node("generate_predictions", safe_predict)
    workflow.add_node("visualize_results", plot_prediction)

    # Define the execution edges
    workflow.set_entry_point("fetch_data")
    workflow.add_edge("fetch_data", "analyze_indicators")
    workflow.add_edge("analyze_indicators", "generate_predictions")
    workflow.add_edge("generate_predictions", "visualize_results")

    return workflow.compile()

# Export the compiled workflow
app = create_workflow()