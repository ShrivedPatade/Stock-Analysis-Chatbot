import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_final_report(state: dict):
    """Uses Gemini API for the final high-level synthesis."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    prompt = f"""
    As a Senior Financial Analyst, provide a concise final report for {state['company_name']} ({state['ticker']}).
    
    CONTEXT:
    - Technical Signals: {state['signals']}
    - Calculated News Sentiment: {state['sentiment']}
    - Current Action Recommendation: {state['recommendation']}
    
    Provide a 3-sentence summary: 
    1. The technical outlook.
    2. How current news impacts this outlook.
    3. A definitive 'Next Step' for an investor.
    """
    
    try:
        response = model.generate_content(prompt)
        state['final_summary'] = response.text
    except Exception as e:
        state['final_summary'] = f"Final summary unavailable: {e}"
        
    return state