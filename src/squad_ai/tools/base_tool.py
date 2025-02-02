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
        pass

    @abstractmethod
    def get_schema(self) -> Dict[str, Any]:
        """Return the tool's schema for OpenAI API."""
        pass