# Predictive Stock Analysis System (Hybrid Agentic Pipeline)

An advanced financial intelligence tool that fuses **Quantitative technical analysis** with **Qualitative news sentiment** to generate actionable trading signals.

## 🚀 Key Innovation: The Hybrid AI Architecture

To overcome API rate limits and maximize analytical precision, this project utilizes a dual-LLM "Brain" strategy:

* **Local Intelligence (Ollama + Qwen2.5-Finance):** Handles high-volume, repetitive tasks. It parses user intent and performs sentiment analysis on 10+ news headlines locally, ensuring zero-latency and bypassing cloud API quotas.
* **Cloud Synthesis (Google Gemini 2.5 Flash):** Reserved for the final "Gold Standard" report. It synthesizes the technical data and local sentiment into a high-reasoning, 3-sentence professional analyst summary.

---

## 🏗️ Technical Pipeline Flow

The system is built as a stateful graph using **LangGraph**, ensuring a reliable and verifiable data lifecycle:

1. **Intent Parsing:** Local Qwen extracts `Ticker`, `Company Name`, and `Period` from natural language.
2. **Data Acquisition:** Fetches historical OHLCV data via `yfinance` with advanced browser impersonation (via `curl_cffi`) to prevent rate-limiting.
3. **Qualitative Retrieval:** Searches **NewsAPI** using the full company name for higher relevancy; results are cached in `retrieved_news.json` for auditing.
4. **Technical Engine:** Calculates SMA 50/200 and RSI indicators to find "Golden Cross" or "Oversold" entry points.
5. **Multi-Modal Synthesis:** Merges technical signals with AI sentiment to generate a final recommendation (e.g., "STRONG BUY").
6. **Visualization:** Generates dual-plot charts (Price + RSI) with specific Buy/Sell markers.

---

## 🛠️ Installation & Setup

### 1. Prerequisites

* **Ollama:** Installed and running locally.
* **Python 3.10+**

### 2. Local Model Setup

```bash
# Pull the finance-optimized model for sentiment and parsing
ollama pull qwen2.5:3b

```

### 3. Environment Configuration

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_google_ai_key
NEWS_API_KEY=your_newsapi_org_key

```

### 4. Run the Pipeline

```bash
python main.py

```

---

## 📈 Performance & Reliability

* **Defensive Engineering:** Includes safety checks at every node to handle missing data or API failures gracefully without crashing.
* **Multi-Modal Precision:** News sentiment acts as a "filter" for technical signals, reducing false-positive BUY signals during bearish news cycles.