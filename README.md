# Squad AI

A modular AI agentic framework.

## Description

Squad AI is a modular framework designed to facilitate the development and deployment of AI agents. The framework is written entirely in Python and aims to provide a flexible and extensible platform for creating intelligent agents.

## Installation

To install Squad AI, clone the repository and install the required dependencies:

```bash
git clone https://github.com/deepak-bhardwaj-ps/squad-ai.git
cd squad-ai
pip install -r requirements.txt
```

### Example: Get Weather

Here is an example of how to use Squad AI to get the current weather:

1. First, ensure you have set up your configuration with the necessary API keys and endpoints.
2. Create a weather agent script like the one below:

```python
from squad_ai import Framework
from squad_ai.interpreter import Interpreter
from squad_ai.persona import Persona
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
    elif "san francisco" in location.lower():
        return json.dumps(
            {"location": "San Francisco", "temperature": "72", "unit": unit}
        )
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
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
    weather_agent = framework.create_agent(
        "Bob",
        Persona(
            "Weather Reporter", "You must reply only with current weather condition."
        ),
        Interpreter(api_key="ollama", base_url="http://localhost:11434/v1"),
        [dynamic_weather],
    )

    weather_agent.perform_task("What is the current temperature in Paris.")
    weather_agent.perform_task("How about Sydney?")
```

3. Run the weather agent script:

```bash
python examples/get_weather.py
```

## Contributing

We welcome contributions to Squad AI! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push your branch to your fork.
4. Open a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on GitHub or contact the repository owner.
