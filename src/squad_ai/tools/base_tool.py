"""
Module Documentation:
---------------------
This module defines the base class `Tool` which serves as a blueprint 
for creating custom tools that can be used with the OpenAI API. 
The `Tool` class requires implementations of two abstract methods: `execute` and `get_schema`.

Classes
-------
- Tool(ABC)
    - Abstract base class for tools.
    - Requires implementation of `execute` and `get_schema` methods.

Methods
-------
- execute(*args, **kwargs) -> str
    - Execute the tool's functionality.
- get_schema() -> Dict[str, Any]
    - Return the tool's schema for OpenAI API.

Usage:
------
Subclasses should inherit from this base class and implement the required 
methods to define specific functionalities that can be invoked via the OpenAI API.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class Tool(ABC):
    """
    Abstract base class for tools.
    This class defines the interface for tools, requiring them to implement
    the `execute` and `get_schema` methods.
    Methods
    -------
    execute(*args, **kwargs) -> str
        Execute the tool's functionality.
    get_schema() -> Dict[str, Any]
        Return the tool's schema for OpenAI API.
    """

    @abstractmethod
    def execute(self, *args, **kwargs) -> str:
        """Execute the tool's functionality."""

    @abstractmethod
    def get_schema(self) -> Dict[str, Any]:
        """Return the tool's schema for OpenAI API."""
