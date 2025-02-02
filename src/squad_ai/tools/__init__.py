"""
This module provides tools for integrating with agents.

It includes base classes and dynamic tool implementations.

Exported Classes:
- Tool: A base class for all tools.
- DynamicTool: A dynamically generated or managed tool class.

Usage:
    >>> from squad_ai.tools import Tool, DynamicTool
"""

from .base_tool import Tool
from .dynamic_tool import DynamicTool

__all__ = [
    "Tool",
    "DynamicTool",
]
