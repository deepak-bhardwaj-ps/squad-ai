"""
Module containing the Agent class which encapsulates an intelligent agent's capabilities.

This module provides a blueprint for creating agents that can perform tasks 
using their persona, a language model (LLM), and tools. Each agent is designed 
to interact with the environment based on its defined role and behavior.
"""

from typing import List, Optional
import json

from squad_ai.prompt_engine import PromptEngine
from squad_ai.persona import Persona
from squad_ai.interpreter import Interpreter
from squad_ai.tools.base_tool import Tool


class Agent:
    """
    An intelligent agent that uses its persona, LLM, and tools to perform tasks.

    Attributes:
        name (str): The name of the agent.
        persona (Persona): The persona that represents the agent's role and behavior.
        llm_wrapper (Interpreter): An interpreter wrapper around an LLM model.
        tools (dict): A dictionary mapping tool names to their instances.
        prompt_engine (PromptEngine): Optional prompt engine for generating prompts.
    """

    def __init__(
        self,
        name: str,
        persona: Persona,
        llm_wrapper: Optional[Interpreter] = None,
        tools: Optional[List[Tool]] = None,
        prompt_engine: Optional[PromptEngine] = None,
    ):
        """Initialize the agent with its components.

        Args:
            name: The name of the agent.
            persona: The persona that represents the agent's role and behavior.
            llm_wrapper: An interpreter wrapper around an LLM model.
            tools: List of tool instances to be used by the agent.
            prompt_engine: Optional prompt engine for generating prompts. Defaults to None.
        """
        self.name = name
        self.persona = persona
        self.llm_wrapper = llm_wrapper or Interpreter(
                api_key="ollama", base_url="http://localhost:11434/v1"
            )
        self.tools = {
            tool.get_schema().get("function")["name"]: tool for tool in tools
        }  # Map tool names to instances
        self.prompt_engine = prompt_engine or PromptEngine()

    def perform_task(self, task: str) -> str:
        """Perform a task using the agent's capabilities.

        Args:
            task: The task to be performed.

        Returns:
            The result of the task as a string.
        """
        # Generate a custom prompt
        prompt = self.prompt_engine.generate_prompt(self.persona, task)

        # Define the tool schemas for the LLM
        tool_schemas = [tool.get_schema() for tool in self.tools.values()]

        # Call the LLM
        response = self.llm_wrapper.interpret(prompt, tool_schemas)

        while True:
            # Process the response
            if response.tool_calls:
                tool_call = response.tool_calls[0]
                # Extract the function name and arguments
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                # Find and execute the corresponding tool
                if function_name in self.tools:
                    tool = self.tools[function_name]
                    print(
                        f"\n{self.name} ({self.persona.name}) is executing tool: {function_name}"
                    )
                    tool_response = tool.execute(**function_args)
                    response = self.llm_wrapper.update_tool_response(
                        tool_call.id, tool_response, tool_schemas
                    )
                else:
                    print(f"Tool '{function_name}' not found.")
                    break
            else:
                print(f"\n{self.name} ({self.persona.name}) says: {response.content}")
                break

        return response.content

    def __str__(self):
        """
        Return a string representation of the agent.

        Returns:
            str: A string representing the agent's name and persona.
        """
        return f"Agent({self.name}, Persona: {self.persona.name})"
