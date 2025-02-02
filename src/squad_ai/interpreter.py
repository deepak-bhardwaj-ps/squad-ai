"""
Interpreter Module

This module provides the functionality to interpret prompts using 
a language model and interact with specified tools.

Classes:
    Interpreter: A class that encapsulates the interaction 
    between the language model and external tools.

Methods:
    - __init__: Initializes an instance of the Interpreter.
    - _create_message: Creates a message dictionary for communication.
    - _call_llm: Internal method to call the language model.
    - interpret: Interprets the given prompt using the specified tools.
    - update_tool_response: Updates the tool response by creating a 
      message and calling the language model.

Usage:
1. Import the Interpreter class from this module.
2. Initialize an instance of the Interpreter with your OpenAI API key and other configurations.
3. Use the interpret method to process prompts and interact with external tools as needed.

Example Usage:
```python
from squad_ai.interpreter import Interpreter

# Initialize the interpreter
interpreter = Interpreter(api_key="YOUR_API_KEY")

# Define some tools (example placeholders)
tools = [
    {"name": "tool1", "description": "Tool 1 description"},
    # Add more tool configurations here
]

# Interpret a prompt with the specified tools
response = interpreter.interpret(prompt="What is the weather like today?", tools=tools)

print(response.content)  # Processed response from the language model
```
"""

from typing import List, Dict, Any
import openai


class Interpreter:
    """
    A class that encapsulates the interaction between the language model and external tools.
    """
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.openai.com/v1",
        model: str = "llama3.1",
    ):
        """Initializes an instance of the Interpreter.
        Args:
            api_key (str): The API key for accessing the language model.
            base_url (str, optional): The base URL for the API endpoint.
            model (str, optional): The model name to be used for processing.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.llm = openai.Client(api_key=api_key, base_url=base_url)
        self.history = []

    def _create_message(
        self, role: str, content: str, call_id: str = None
    ) -> Dict[str, Any]:
        """
        Creates a message dictionary for communication.

        Args:
            role (str): The role of the message sender ("user" or "tool").
            content (str): The content of the message.
            call_id (str, optional): A unique identifier for the call.

        Returns:
            Dict[str, Any]: The created message dictionary.
        """
        message = {"role": role, "content": content}
        if call_id:
            message["tool_call_id"] = call_id
        return message

    def _call_llm(self, message: Dict[str, Any], tools: List[Dict[str, Any]]):
        """Internal method to call the LLM and return its response."""
        self.history.append(message)
        response = self.llm.chat.completions.create(
            model=self.model,
            messages=self.history,
            tools=tools,
            tool_choice="auto",
        )
        response_message = response.choices[0].message
        self.history.append(
            self._create_message(
                role=response_message.role, content=response_message.content
            )
        )
        return response_message

    def interpret(self, prompt: str, tools: List[Dict[str, Any]]):
        """
        Interprets the given prompt using the specified tools.
        Args:
            prompt (str): The input prompt to be interpreted.
            tools (List[Dict[str, Any]]): A list of tools, where each tool is represented 
                as a dictionary containing tool-specific information.
        Returns:
            Any: The result of the interpretation process, as returned by the language model.
        """

        message = self._create_message(role="user", content=prompt)
        return self._call_llm(message=message, tools=tools)

    def update_tool_response(
        self, call_id: str, result: str, tools: List[Dict[str, Any]]
    ):
        """
        Updates the tool response by creating a message and calling the language model.
        Args:
            call_id (str): The unique identifier for the call.
            result (str): The result of tool call to be sent to the language model.
            tools (List[Dict[str, Any]]): A list of tools with their configurations.
        Returns:
            Any: The response from the language model.
        """

        message = self._create_message(role="tool", content=result, call_id=call_id)
        return self._call_llm(message=message, tools=tools)
