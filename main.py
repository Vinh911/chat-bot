from fastapi import FastAPI
from src.service.CSVService import CSVService
from src.controller.ApiController import ApiController

print("Loading data...", flush=True)
csv_service = CSVService("data/dataset.csv")

@app.on_event("startup")
async def load_csv_data():
    """Load and process the CSV file during startup."""
    csv_service.read_and_process_csv()
    print("CSV data loaded and processed.", flush=True)

print("starting the application", flush=True)
app = FastAPI()
ApiController(app)