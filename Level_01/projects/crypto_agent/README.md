# 📊 Crypto Agent using Gemini 2.0 Flash & Binance API
---

This guide helps you **step-by-step** to build a crypto agent that can respond with **live cryptocurrency prices** using:

- **Gemini 2.0 Flash** (OpenAI-compatible model)
- **Binance API** (for real-time data)
- **Tool calling functionality**

---

## 🎯 Goal
---

Create an intelligent agent that answers questions like:

> 💬 "What's the current rate of BTCUSDT?"

---

## 🧰 What You Need
---

- Python basics
- An API key for **Gemini** (get from Google AI Studio)
- Basic knowledge of how APIs work
- `requests`, `python-dotenv`, and an agent framework (provided or custom)

---

## 🪜 Step-by-Step Instructions
---

### ✅ Step 1: Project Setup
---

1. Create a folder for your project.
2. Initialize uv.
3. Run this to install dependencies:
   uv add openai-agents
4. Inside the root, create a .env file:
   GEMINI_API_KEY=your_gemini_api_key_here

### ✅ Step 2: Load the Gemini API Key
---

Use dotenv to read the API key from .env.
Add a check: if the key is missing, stop the program.
📌 Why? So your API key is not exposed or hardcoded.

### ✅ Step 3: Configure Gemini 2.0 Flash Model
---

Set up AsyncOpenAI or a compatible client using:

1. API key
2. Base URL: https://generativelanguage.googleapis.com/v1beta/openai/
3. Model name: "gemini-2.0-flash"
📌 Why? This allows the agent to think and respond like a chatbot.

### ✅ Step 4: Understand Binance Symbols
---

Binance uses specific formats for trading pairs:

Example	Meaning:
1. BTCUSDT	(Bitcoin to US Dollar)
2. ETHUSDT	(Ethereum to US Dollar)
3. BTCETH	(Bitcoin to Ethereum)
📌 Why? You must use the correct symbol in API requests.

### ✅ Step 5: Create a Tool to Get Crypto Prices
---

Make a Python function that:

1. Takes a symbol (e.g. BTCUSDT)

2. Sends a request to:
  https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
  Returns the price as a formatted string

3. Use a decorator like @function_tool so the agent can use this tool.
📌 Why? This allows real-time data fetching via API.

### ✅ Step 6: Build the Crypto Agent
---

Define an agent with:

1. A name (e.g. "Crypto Agent")
2. Clear instructions (e.g. “Get live crypto rates”)
3. The crypto price tool added to its tools
📌 Why? This gives your agent a purpose and power to act.

### ✅ Step 7: Ask the Agent Questions
---

Use a runner method like Runner.run_sync(...)

Pass questions like:
What is the rate of BTCUSDT?
What is the rate of ETHUSDT?
📌 Why? This runs your agent and gets live answers.

### ✅ Step 8: Print the Final Answer
---
The final response will look like:

The current rate of BTCUSDT is $65,000.45
📌 Why? This is the final user-facing output.

---

**Crypto Currency API that fetches that realtime data of Digital Coins**

API Endpoint: Get all coins: https://api.binance.com/api/v3/ticker

Get coin by Symbol: https://api.binance.com/api/v3/ticker/price?symbol={currency}