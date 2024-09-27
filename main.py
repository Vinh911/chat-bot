from fastapi import FastAPI
from src.controller.ApiController import ApiController

app = FastAPI()

ApiController(app)