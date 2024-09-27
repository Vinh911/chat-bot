from fastapi import APIRouter, Depends
from src.model.MessageModel import MessageModel
from src.service.MessageService import MessageService

class ApiController:
    """
    This controller is responsible for setting up the API routes and handling
    the requests.
    """
    def __init__(self, app, message_service: MessageService):
        self.message_service = message_service
        router = APIRouter()
        
        @router.post("/sendMessage")
        async def send_message(message: MessageModel):
            """
            This route accepts a message input, performs a semantic search on the dataset,
            and returns a response generated by a local LLM based on the most relevant data.

            Args:
                message (MessageModel): The input message to be processed.

            Returns:
                dict: A dictionary containing the generated response from the LLM.
            """
            response = message_service.processMessage(message.message)

            return {"response": response}
        
        app.include_router(router)