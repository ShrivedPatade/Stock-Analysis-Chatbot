import google.generativeai as genai
from lgWorkflow import workflow

# Configure Gemini API Key (Assume it's set as an environment variable)
import os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def query_llm(prompt: str):
    """Query Google's Gemini AI to extract stock symbol and period."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

def parse_user_input(user_input: str):
    """LLM to extract the stock ticker, timeframe, and required analysis from user input."""
    llm_response = query_llm(f""" Extract and return the company name that appears first, time period, and the type of analysis requested.
                             Convert the company name to an appropriate stock ticker code and return in the form 'CompanyTickerCode Period AnalysisType', 
                             example 'GOOGL 24mo moving_average' or 'GOOGL 24mo volume_trend' for Google and 2 years or 24 months and moving average or volume trend.
                             If the period is less than a month then return 1mo, if it is in years convert into months then return numbermo.
                             If no analysis is specified, return 'basic' as default. '{user_input}'""")
    parts = llm_response.split()
    print(parts)
    ticker = parts[0].replace(r'[^\w]', '') if len(parts) > 0 else "AAPL"
    period = parts[1] if len(parts) > 1 else "6mo"
    analysis_type = parts[2:] if len(parts) > 2 else ["basic"]
    
    return {"ticker": ticker, "period": period, "analysis_type": analysis_type}  # Default to AAPL, 6mo, and basic analysis if parsing fails

def getResponse(user_input: str):
    """Get the response from the workflow."""
    parsed_input = parse_user_input(user_input)
    response = workflow.invoke(parsed_input)
    return response

if __name__ == "__main__":
    # user_input =  Show me the stock prices of Google for last 2 years with volume trend and moving averages
    getResponse(input("Prompt: ").strip())