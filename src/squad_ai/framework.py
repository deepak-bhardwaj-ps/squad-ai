from typing import List

from . import PromptEngine, Persona, Interpreter, Tool, Agent


class Framework:
    def __init__(self):
        self.agents = {}

    def create_agent(
        self,
        name: str,
        persona: Persona,
        interpreter: Interpreter,
        tools: List[Tool],
        prompt_engine: PromptEngine = None,
    ) -> Agent:
        """
        Creates and registers a new agent.
        Args:
            name (str): The name of the agent.
            persona (Persona): The persona of the agent.
            interpreter (Interpreter): The interpreter used by the agent.
            tools (List[Tool]): A list of tools available to the agent.
            prompt_engine (PromptEngine, optional): The prompt engine for the agent. Defaults to None.
        Returns:
            Agent: The created agent instance.
        Raises:
            ValueError: If an agent with the same name already exists.
        """

        # Check if an agent with the same name already exists
        if name in self.agents:
            raise ValueError(f"An agent with the name {name} already exists.")

        agent = Agent(name, persona, interpreter, tools, prompt_engine)
        self.agents[name] = agent

        return agent

    def list_agents(self):
        """List all registered agents."""
        for _, agent in self.agents.items():
            print(agent)
