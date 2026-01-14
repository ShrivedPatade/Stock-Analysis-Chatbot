import google.generativeai as genai
from config import GEMINI_API_KEY, DEFAULT_PERIOD
from workflow import app

# Configure AI
genai.configure(api_key=GEMINI_API_KEY)

def parse_request(user_prompt: str):
    """Uses LLM to turn a sentence into structured data (Ticker/Period)."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = f"""
    Extract the stock ticker symbol and the requested time period from this prompt: "{user_prompt}"
    Return the result strictly in this format: TICKER PERIOD
    Example: "Analyze Google for 2 years" -> GOOGL 2y
    If no period is found, use {DEFAULT_PERIOD}.
    """
    
    response = model.generate_content(prompt).text.strip().split()
    ticker = response[0] if len(response) > 0 else "AAPL"
    period = response[1] if len(response) > 1 else DEFAULT_PERIOD
    
    return {"ticker": ticker, "period": period}

def run_pipeline():
    print("--- Predictive Stock Analysis System ---")
    user_input = input("What stock would you like to analyze? ")
    
    # 1. Parse Input
    print(f"Intelligently parsing: '{user_input}'...")
    initial_state = parse_request(user_input)
    
    # 2. Run Workflow
    print(f"Starting pipeline for {initial_state['ticker']} over {initial_state['period']}...")
    final_output = app.invoke(initial_state)
    
    # 3. Final Summary
    print("\nAnalysis Complete!")
    print(f"Detected {len(final_output['signals'])} major trading signals.")
    # The plot will display automatically from the 'visualize_results' node

if __name__ == "__main__":
    run_pipeline()