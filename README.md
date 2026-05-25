# 🌤️ AutoGen-FastAPI-WeatherAgent

An autonomous, production-ready, full-stack AI Agent application designed to fetch real-time weather data based on dynamic user queries. This project marks the beginning of my journey into the ecosystem of **Agentic AI**, utilizing a decoupled architecture with a FastAPI backend and a Streamlit frontend.

---

## 🚀 Key Features

* **Autonomous Reasoning:** Driven by Microsoft's AutoGen framework and `gpt-4o`, the agent dynamically evaluates user intent, handles guardrails, and decides when to invoke external tools.
* **Intelligent Guardrails:** The system exhibits agentic behavior by validating input scale (e.g., handling broad queries like "America" or "India" by asking for clarification rather than executing broken API calls).
* **Asynchronous Execution:** Built with an asynchronous, non-blocking HTTP client (`httpx`) to maintain scalable and rapid tool execution.
* **Decoupled Architecture:** Features a completely separated Full-Stack system (FastAPI serving the model core and Streamlit presenting a clean user conversational layer).

---

## 🛠️ Tech Stack

* **Agentic Framework:** Microsoft AutoGen (AgentChat)
* **LLM Engine:** OpenAI `gpt-4o`
* **Backend Framework:** FastAPI & Uvicorn Server
* **Frontend UI:** Streamlit
* **HTTP Client:** HTTPX (Async)
* **Data Validation:** Pydantic
* **Environment Management:** Python-dotenv


---

## 📸 Application Screenshots & Output

Here is how the application workflow operates seamlessly between the Streamlit user interface and the autonomous AutoGen backend:

### 1. Streamlit Interface & Agent Response
This screen demonstrates the end-user chat interface where the agent intelligently processes queries and returns structured weather parameters.

![Streamlit Interface Output](./output%201.PNG)

### 2. FastAPI Backend & Agentic Reasoning Log
This screen captures the backend execution flow, showcasing how the Microsoft AutoGen agent invokes the custom tools and logs reasoning streams.

![FastAPI Backend Logs](./output%202.PNG)

---

## 📁 Project Structure

```text
AutoGen-FastAPI-WeatherAgent/
│
├── app.py                # FastAPI Backend Server & AutoGen Agent Setup
├── frontend.py           # Streamlit Web User Interface
├── .env.example          # Template for required environment variables
├── .gitignore            # Strictly prevents leaking credentials and environments
└── requirements.txt      # List of dependencies
