"""
This module contains an example of using the Squad AI framework to get current weather conditions.
"""

import json

from squad_ai import Framework
from squad_ai.agent import AgentConfig
from squad_ai.interpreter import Interpreter
from squad_ai.persona import Persona
from squad_ai.prompt_engine import PromptEngine
from squad_ai.tools.dynamic_tool import DynamicTool


def get_current_weather(location: str, unit: str = "fahrenheit") -> str:
    """
    Get the current weather in a given location

    Parameters:
    location (str): The city and state, e.g. San Francisco, CA
    unit (str): The unit of temperature, either 'celsius' or 'fahrenheit'
    """

    print(f"Getting the current weather in {location}...")

    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    if "san francisco" in location.lower():
        return json.dumps(
            {"location": "San Francisco", "temperature": "72", "unit": unit}
        )
    if "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    return json.dumps({"location": location, "temperature": "unknown"})


if __name__ == "__main__":

    dynamic_weather = DynamicTool(
        get_current_weather, description="Get the current weather in a given location."
    )

    # Create LLM wrappers
    openai_interpreter = Interpreter(
        api_key="ollama", base_url="http://localhost:11434/v1"
    )

    # Create the framework
    framework = Framework()

    # Create agents
    weather_agent_persona = Persona(
        name="Weather Reporter",
        description="You must reply only with current weather condition.",
    )

    weather_agent = framework.create_agent(
        "Bob",
        AgentConfig(
            persona=weather_agent_persona,
            llm_wrapper=openai_interpreter,
            tools=[dynamic_weather],
            prompt_engine=PromptEngine(),
        ),
    )

    weather_agent.perform_task("What is the current temprature in Paris.")
    weather_agent.perform_task("How about Sydney?")
