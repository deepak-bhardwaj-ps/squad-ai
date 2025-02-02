"""
This module defines a DynamicTool class that wraps a callable function and 
dynamically generates a schema based on the function's signature and docstring.

Classes:
    MissingParameterDescriptionError(Exception):

    DynamicTool(Tool):
        A class that wraps a callable function and dynamically generates a schema 
        based on the function's signature and docstring.
"""

import re
import inspect
from typing import Callable, Dict, Any
from .base_tool import Tool


class MissingParameterDescriptionError(Exception):
    """
    Custom exception raised when there is a missing parameter description.
    """


class DynamicTool(Tool):
    """
    DynamicTool is a class that wraps a callable function and dynamically
    generates a schema based on the function's signature and docstring.
    Attributes:
        name (str): Name of the tool.
        description (str): Description of the tool.
        _schema (Dict[str, Any]): The dynamically generated schema for the tool.
    Methods:
        __init__(func: Callable, name: str = None, description: str = None):
        _parse_docstring() -> Dict[str, str]:
            Parse the docstring of the function to extract parameter descriptions.
        _get_parameter_type(param: inspect.Parameter) -> str:
            Extract the type of a parameter from its annotation.
            Defaults to 'string' if no type is specified.
        _generate_schema() -> Dict[str, Any]:
        execute(*args, **kwargs) -> str:
        get_schema() -> Dict[str, Any]:
    """

    def __init__(self, func: Callable, name: str = None, description: str = None):
        """
        Initialize a dynamic tool with a callable function.

        Args:
            func (Callable): The callable function to wrap.
            name (str, optional): Name of the tool. Defaults to the function's name.
            description (str, optional): Description of the tool.
        """
        self.func = func
        self.name = name or func.__name__
        self.description = description or func.__doc__ or "No description provided."
        self._schema = self._generate_schema()

    def _parse_docstring(self) -> Dict[str, str]:
        docstring = self.func.__doc__
        lines = docstring.strip().split("\n")
        param_descriptions = {}
        param_section = False

        for line in lines:
            line = line.strip()
            if line.startswith("Parameters:"):
                param_section = True
                continue
            if param_section and line:
                if re.match(r"\w+\s*\(\w+\):", line):
                    param, desc = line.split(":", 1)
                    param_name, _ = param.split()
                    param_descriptions[param_name.strip()] = desc.strip()
                else:
                    break
        if not param_descriptions:
            raise MissingParameterDescriptionError(
                f"The function '{self.func.__name__}' has no valid parameter descriptions."
            )

        return param_descriptions

    def _get_parameter_type(self, param: inspect.Parameter) -> str:
        """
        Extract the type of a parameter from its annotation.
        If no type is specified, default to 'string'.

        Args:
            param (inspect.Parameter): The parameter to analyze.

        Returns:
            str: The type of the parameter as a string.
        """
        if param.annotation is not inspect.Parameter.empty:
            return param.annotation.__name__
        return "str"

    def _generate_schema(self) -> Dict[str, Any]:
        """
        Dynamically generate a schema for the tool based on the function's signature.

        Returns:
            Dict[str, Any]: The schema for the tool.
        """
        sig = inspect.signature(self.func)
        param_descriptions = self._parse_docstring()
        parameters = {
            name: {
                "type": self._get_parameter_type(param),
                "description": param_descriptions.get(name, "No description provided."),
            }
            for name, param in sig.parameters.items()
        }

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": parameters,
                    "required": list(parameters.keys()),
                },
            },
        }

    def execute(self, *args, **kwargs) -> str:
        """
        Execute the wrapped callable function.

        Args:
            *args: Positional arguments passed to the function.
            **kwargs: Keyword arguments passed to the function.
        """
        print(
            f"Executing dynamic tool '{self.name}' with args: {args}, kwargs: {kwargs}"
        )
        return self.func(*args, **kwargs)

    def get_schema(self) -> Dict[str, Any]:
        """
        Return the dynamically generated schema for the tool.

        Returns:
            Dict[str, Any]: The schema for the tool.
        """
        return self._schema
