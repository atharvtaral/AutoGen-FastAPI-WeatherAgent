import streamlit as str
import httpx

# 1. Page Configuration (Theme and Title)
str.set_page_config(
    page_title="Agentic Weather AI",
    page_icon="🌤️",
    layout="centered"
)

# 2. Header and Setup Design
str.title("🌤️ Agentic Weather AI Interface")
str.markdown("---")
str.write("An intelligent personal weather assistant powered by Microsoft AutoGen and FastAPI!")

# 3. Backend FastAPI Server URL
FASTAPI_URL = "http://127.0.0.1:8000/weather"

# 4. User Input Field for City Name
city_input = str.text_input(
    label="Which city's weather do you want to check? Enter the name:",
    placeholder="e.g., Parner, Pune, Mumbai, London..."
)

# 5. Execution Trigger on Button Click
if str.button("Check Weather 🚀", use_container_width=True):
    if city_input.strip() == "":
        str.warning("Please enter a city name first!")
    else:
        # Visual loading indicator while fetching agent response
        with str.spinner(f"My AI Agent is collecting data for {city_input}... Please wait..."):
            try:
                # Establishing connection and sending POST request to FastAPI
                payload = {"city": city_input}
                response = httpx.post(FASTAPI_URL, json=payload, timeout=30.0)
                
                if response.status_code == 200:
                    result = response.json()
                    agent_reply = result.get("agent_response", "No response received from the agent.")
                    
                    # Displaying the final processed output cleanly
                    str.success("🎯 Agent Response:")
                    str.info(agent_reply)
                    
                else:
                    str.error(f"Backend server returned an error code: {response.status_code}")
                    
            except httpx.ConnectError:
                str.error("❌ Connection Error: Your FastAPI server is not running! Please execute `python app.py` first.")
            except Exception as e:
                str.error(f"An unexpected error occurred: {str(e)}")

# 6. Footer (Credits)
str.markdown("---")
str.caption("Built with 💻 by Atharv | Powered by AutoGen & FastAPI")