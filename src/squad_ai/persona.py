class Persona:
    """
    A class to represent a persona with a name and description.

    Attributes:
    ----------
    name : str
        The name of the persona.
    description : str
        A brief description of the persona.

    Methods:
    -------
    __str__():
        Returns a string representation of the persona.
    """

    def __init__(self, name: str, description: str):
        """
        Constructs all the necessary attributes for the persona object.

        Parameters:
        ----------
        name : str
            The name of the persona.
        description : str
            A brief description of the persona.
        """
        self.name = name
        self.description = description

    def __str__(self):
        """
        Returns a string representation of the persona.

        Returns:
        -------
        str
            A string in the format "name: description".
        """
        return f"{self.name}: {self.description}"
