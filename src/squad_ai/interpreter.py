import openai
from typing import List, Dict, Any


class Interpreter:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.openai.com/v1",
        model: str = "llama3.1",
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.llm = openai.Client(api_key=api_key, base_url=base_url)
        self.history = []

    def _create_message(
        self, role: str, content: str, call_id: str = None
    ) -> Dict[str, Any]:
        """Create a message dictionary."""
        message = {"role": role, "content": content}
        if call_id:
            message["tool_call_id"] = call_id
        return message

    def _call_llm(self, message: Dict[str, Any], tools: List[Dict[str, Any]]):
        """Internal method to call the LLM and return its response."""
        self.history.append(message)
        response = self.llm.chat.completions.create(
            model=self.model,
            messages=self.history,
            tools=tools,
            tool_choice="auto",
        )
        response_message = response.choices[0].message
        self.history.append(
            self._create_message(
                role=response_message.role, content=response_message.content
            )
        )
        return response_message

    def interpret(self, prompt: str, tools: List[Dict[str, Any]]):
        """
        Interprets the given prompt using the specified tools.
        Args:
            prompt (str): The input prompt to be interpreted.
            tools (List[Dict[str, Any]]): A list of tools, where each tool is represented as a dictionary containing tool-specific information.
        Returns:
            Any: The result of the interpretation process, as returned by the language model.
        """

        message = self._create_message(role="user", content=prompt)
        return self._call_llm(message=message, tools=tools)

    def update_tool_response(
        self, call_id: str, result: str, tools: List[Dict[str, Any]]
    ):
        """
        Updates the tool response by creating a message and calling the language model.
        Args:
            call_id (str): The unique identifier for the call.
            result (str): The result of tool call to be sent to the language model.
            tools (List[Dict[str, Any]]): A list of tools with their configurations.
        Returns:
            Any: The response from the language model.
        """

        message = self._create_message(role="tool", content=result, call_id=call_id)
        return self._call_llm(message=message, tools=tools)
