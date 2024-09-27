from src.service.LlmService import LlmService

class MessageService:
    """
    This service is responsible for handling the processing of incoming messages.
    It performs the necessary operations to generate a response based on the given input message.
    """

    def __init__(self, llm_service: LlmService):
        self.llm_service = llm_service

    def processMessage(self, message: str) -> str:
        """
        Processes the given message and generates an appropriate response.

        Args:
            message (str): The input message to be processed.

        Returns:
            str: A response based on the processed message.
        """
        response = response = self.llm_service.generate_prompt(message)
        # TODO: implement semantic search
        return response