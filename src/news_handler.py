import json
import os
import ollama
import google.generativeai as genai
from newsapi import NewsApiClient
from config import NEWS_API_KEY

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def fetch_news(state: dict):
    """Retrieves news based on company name and stores it in JSON."""
    query = state.get(state['company_name'], state["ticker"])
    print(f"Searching news for: {query}...")
    
    try:
        response = newsapi.get_everything(
            q=query,
            language='en',
            sort_by='relevancy',
            page_size=10
        )
        
        articles = response.get('articles', [])
        
        # Error Handling: Manage no news article retrieved condition
        if not articles:
            print(f"No news articles found for {query}.")
            state["news"] = []
            return state

        # Extract headlines and metadata
        news_data = []
        for a in articles:
            news_data.append({
                "title": a['title'],
                "description": a.get('description', ''),
                "url": a.get('url', ''),
                "publishedAt": a.get('publishedAt', '')
            })

        # JSON Storage: Store as a way to check
        storage_path = "retrieved_news.json"
        with open(storage_path, "w") as f:
            json.dump({"query": query, "count": len(news_data), "articles": news_data}, f, indent=4)
        
        print(f"Successfully stored {len(news_data)} articles in {storage_path}.")
        state["news"] = [item['title'] for item in news_data]
        return state

    except Exception as e:
        print(f"Error retrieving news: {e}")
        state["news"] = []
        return state

def analyze_sentiment(state: dict):
    """Quantifies sentiment using local Qwen2.5:3b."""
    if not state.get("news"):
        return {**state, "sentiment": 0.0}

    headlines = "\n- ".join(state["news"])
    prompt = f"Analyze these headlines for {state['company_name']} and provide a sentiment score from -1.0 to 1.0. Return ONLY the number: \n{headlines}"
    
    try:
        response = ollama.chat(model='qwen2.5:3b', messages=[
            {'role': 'user', 'content': prompt}
        ])
        # Extract only the float from the response
        sentiment = float(''.join(c for c in response['message']['content'] if c in '0123456789.-'))
    except:
        sentiment = 0.0
        
    return {**state, "sentiment": sentiment}