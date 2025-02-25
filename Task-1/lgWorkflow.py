import yfinance as yf
import pandas as pd
from typing import TypedDict
from langgraph.graph import StateGraph

# Custom Dictionary Structure to store relevant data
class StockState(TypedDict):
    ticker: str
    period: str
    data: pd.DataFrame
    analysis_type: list

# import all functions
from fetchData import fetch_stock_data
from analyzeData import analyze_stock_data
from plotData import plot_stock_data


# Set up the graph workflow
graph = StateGraph(StockState)
# graph nodes
graph.add_node("fetch_data", fetch_stock_data)
graph.add_node("analyze_data", analyze_stock_data)
graph.add_node("plot_data", plot_stock_data)

# set entry point
graph.set_entry_point("fetch_data")
# graph edges
graph.add_edge("fetch_data", "analyze_data")
graph.add_edge("analyze_data", "plot_data")

# Compile the graph
workflow = graph.compile()
