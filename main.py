from fastapi import FastAPI
from src.service.CSVService import CSVService
from src.service.EmbeddingService import EmbeddingService
from src.service.LlmService import LlmService
from src.service.MessageService import MessageService
from src.controller.ApiController import ApiController

csv_service = CSVService("data/dataset.csv")
# embedding_service = EmbeddingService("sentence-transformers/msmarco-distilbert-base-v3")
llm_service = LlmService("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

app = FastAPI()

message_service = MessageService(llm_service)

@app.on_event("startup")
async def initialize_application():
    """Load and process the CSV file, starts the local models."""
    print("Init application...", flush=True)

    csv_service.read_and_process_csv()

    # TODO: embedding_service.load_model()
    llm_service.load_model()

print("starting the application", flush=True)

ApiController(app, message_service)