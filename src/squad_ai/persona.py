"""
This module defines the Persona class, which represents a persona with a name and description.

Classes:
---------
- Persona: A class to represent a persona with a name and description.
"""

from pydantic import BaseModel

class Persona(BaseModel):
    """
    A class representing a persona with a name and description.

    Attributes:
    -----------
    name (str): The name of the persona.
    description (str): The description of the persona.
    """

    name: str
    description: str
