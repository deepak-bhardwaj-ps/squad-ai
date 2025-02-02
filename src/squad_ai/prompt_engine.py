from squad_ai.persona import Persona


class PromptEngine:
    """
    PromptEngine is a class responsible for generating custom prompts based on a given persona and task.

    Attributes:
        DEFAULT_TEMPLATE (str): The default template string used for generating prompts.

    Methods:
        __init__(self, prompt_template=None):
            Initializes the PromptEngine with a specified template or the default template if none is provided.

        generate_prompt(self, persona: Persona, task: str) -> str:
            Generates a custom prompt based on the agent's persona using the specified template.

            Parameters:
                persona (Persona): The persona of the agent.
                task (str): The task the agent is performing.

            Returns:
                str: A custom prompt based on the provided persona and task.
    """

    # Default template for generating prompts
    DEFAULT_TEMPLATE = "As a {name}, your task is: {task}. Remember, {description}."

    def __init__(self, prompt_template=None):
        if prompt_template is None:
            self.prompt_template = self.DEFAULT_TEMPLATE
        else:
            self.prompt_template = prompt_template

    def generate_prompt(self, persona: Persona, task: str) -> str:
        """
        Generates a prompt string based on the given persona and task.
        Args:
            persona (Persona): An instance of the Persona class containing the name and description.
            task (str): The task description to be included in the prompt.
        Returns:
            str: A formatted prompt string.
        """

        return self.prompt_template.format(
            name=persona.name, task=task, description=persona.description
        )
