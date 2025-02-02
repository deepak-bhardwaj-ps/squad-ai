"""
This module provides a framework for creating and managing agents. 
Each agent can have its own persona, interpreter, tools, and optional prompt engine.

Classes:
    - Framework: Manages and creates agents.
    - Agent: Represents an individual agent in the system.

Methods:
    - `create_agent`: Creates and registers a new agent with specified details.
    - `list_agents`: Lists all registered agents.
"""

from squad_ai.agent import AgentConfig

from . import Agent


class Framework:
    """
    A class for managing and creating agents.
    """

    def __init__(self):
        self.agents = {}

    def create_agent(
        self,
        name: str,
        config: AgentConfig,
    ) -> Agent:
        """
        Creates and registers a new agent.
        Args:
            name (str): The name of the agent.
            persona (Persona): The persona of the agent.
            interpreter (Interpreter): The interpreter used by the agent.
            tools (List[Tool]): A list of tools available to the agent.
            prompt_engine (PromptEngine, optional): The prompt engine for the agent.
        Returns:
            Agent: The created agent instance.
        Raises:
            ValueError: If an agent with the same name already exists.
        """

        # Check if an agent with the same name already exists
        if name in self.agents:
            raise ValueError(f"An agent with the name {name} already exists.")

        agent = Agent(name, config)
        self.agents[name] = agent

        return agent

    def list_agents(self):
        """List all registered agents."""
        for _, agent in self.agents.items():
            print(agent)
