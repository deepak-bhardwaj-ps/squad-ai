"""
This module provides a framework for creating and managing agents. 
Each agent can have its own persona, interpreter, tools, and optional prompt engine.

Classes:
    - Framework: Manages and creates agents.
    - Agent: Represents an individual agent in the system.

Module Documentation:
    This module is part of the SQUAD AI framework, designed to facilitate 
    the creation and management of intelligent agents. 
    
    It includes classes for managing agents and methods for creating and listing those agents.
"""

from .agent import Agent
from .persona import Persona
from .interpreter import Interpreter
from .tools.base_tool import Tool
from .prompt_engine import PromptEngine
from .framework import Framework

__all__ = [
    "Agent",
    "Persona",
    "Interpreter",
    "Tool",
    "PromptEngine",
    "Framework",
]
