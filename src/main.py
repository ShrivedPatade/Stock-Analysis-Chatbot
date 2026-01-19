import ollama
from config import DEFAULT_PERIOD
from workflow import app

def parse_request(user_prompt: str):
    print(f"Locally parsing intent: '{user_prompt}'...")
    
    prompt = f"""
    You are a financial data extractor. Extract the CORRECT stock ticker symbol, the full company name, and the time period.
    
    Examples:
    - "Analyze apple" -> AAPL | Apple Inc. | 1y
    - "Google for 6 months" -> GOOGL | Alphabet Inc. | 6mo
    - "Check Nvidia performance" -> NVDA | NVIDIA Corporation | 1y
    
    Now process this: "{user_prompt}"
    Return strictly in this format: TICKER | COMPANY_NAME | PERIOD
    """
    
    try:
        response = ollama.chat(model='qwen2.5:3b', messages=[
            {'role': 'user', 'content': prompt}
        ])
        # Clean the response to ensure no extra text is included
        parts = response['message']['content'].strip().split(" | ")
        return {
            "ticker": parts[0] if len(parts) > 0 else "AAPL",
            "company_name": parts[1] if len(parts) > 1 else "Apple Inc",
            "period": parts[2] if len(parts) > 2 else DEFAULT_PERIOD
        }
    except Exception as e:
        print(f"Local parse failed, using defaults: {e}")
        return {"ticker": "AAPL", "company_name": "Apple Inc", "period": DEFAULT_PERIOD}

def run_pipeline():
    print("--- Hybrid Predictive Stock System ---")
    user_input = input("What stock would you like to analyze? ")
    initial_state = parse_request(user_input)
    
    print(f"Starting pipeline for {initial_state['company_name']}...")
    final_output = app.invoke(initial_state)
    
    print("\n" + "="*30)
    print("FINAL ANALYSIS REPORT")
    print("="*30)
    print(final_output.get('final_summary', "No summary generated."))
    
if __name__ == "__main__":
    run_pipeline()