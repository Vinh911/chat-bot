from fastapi import APIRouter

class ApiController:
    def __init__(self, app) -> None:
        router = APIRouter()

        @router.get("/")
        async def hello_word():
            return {"message": "hello World!"}
        
        app.include_router(router)