import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.agents import AssistantAgent

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
weather_api_key = os.getenv("OPENWEATHER_API_KEY")

# 1. Define the FastAPI Application
app = FastAPI(
    title="Agentic Weather API Server",
    description="FastAPI backend running a Microsoft AutoGen Weather Agent",
    version="1.0"
)

# 2. Setup the LLM Model Client
model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=api_key
)

# 3. Define the Weather Retrieval Tool Function
async def get_weather(city: str) -> str:
    """Fetch the weather from OpenWeatherMap API for a given city"""
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": weather_api_key,
            "units": "metric"
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            
        data = response.json()
        if response.status_code != 200 or "weather" not in data:
            return f"Could not fetch weather for '{city}'."
        
        desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        location = data["name"]
        return f"{location}: {desc}, {temp}°C"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

# 4. Setup the AutoGen Assistant Agent
agent = AssistantAgent(
    name="weather_agent",
    model_client=model_client,
    tools=[get_weather],
    system_message=(
        "You are a helpful weather assistant. If the user asks about weather, "
        "use the 'get_weather' tool to find real-time information."
    ),
    reflect_on_tool_use=True,
)

# 5. Define Pydantic Model for Input Data Validation
class WeatherRequest(BaseModel):
    city: str

# 6. Main API Endpoint for Agent Execution
@app.post("/weather")
async def ask_weather_agent(request: WeatherRequest):
    try:
        # Using agent.run instead of run_stream to return the final structured response directly to the API
        result = await agent.run(task=f"What is the weather in {request.city}?")
        
        # Extract the content of the last message from the agent execution history
        final_response = result.messages[-1].content
        return {
            "status": "success",
            "city": request.city,
            "agent_response": final_response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent Execution Error: {str(e)}")

# 7. Main Block to Run the Local Uvicorn Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)