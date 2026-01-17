from typing import TypedDict, List
import pandas as pd
from langgraph.graph import StateGraph
from data_loader import fetch_stock_data
from indicators import apply_indicators
from engine import generate_signals
from visualizer import plot_prediction
from news_handler import fetch_news, analyze_sentiment
from summary_engine import generate_final_report

# Define the structured state for the graph including news fields
class StockState(TypedDict):
    ticker: str
    company_name: str
    period: str
    data: pd.DataFrame
    news: List[str]
    sentiment: float
    signals: List[dict]
    recommendation: str
    final_summary: str # New field for Gemini output

def create_workflow():
    workflow = StateGraph(StockState)

    # Nodes
    workflow.add_node("fetch_data", fetch_stock_data)
    workflow.add_node("fetch_news", fetch_news)
    workflow.add_node("analyze_indicators", lambda state: {**state, "data": apply_indicators(state["data"])})
    workflow.add_node("sentiment_analysis", analyze_sentiment)
    workflow.add_node("generate_predictions", generate_signals)
    workflow.add_node("gemini_summary", generate_final_report) # Final high-reasoning node
    workflow.add_node("visualize_results", plot_prediction)

    # Edges
    workflow.set_entry_point("fetch_data")
    workflow.add_edge("fetch_data", "fetch_news")
    workflow.add_edge("fetch_news", "analyze_indicators")
    workflow.add_edge("analyze_indicators", "sentiment_analysis")
    workflow.add_edge("sentiment_analysis", "generate_predictions")
    workflow.add_edge("generate_predictions", "gemini_summary")
    workflow.add_edge("gemini_summary", "visualize_results")

    return workflow.compile()

app = create_workflow()