import csv
from typing import List, Dict

class CSVService:
    """
    This service is responsible for reading a CSV file, processing its content,
    and storing the data in-memory. This service follows the Singleton pattern to ensure
    only one instance is used throughout the application.
    """
        
    _instance = None
    data: List[Dict[str, str]] = []

    def __new__(cls, file_path: str):
        if cls._instance is None:
            cls._instance = super(CSVService, cls).__new__(cls)
            cls._instance.file_path = file_path
        return cls._instance
    
    def read_and_process_csv(self) -> None:
        """Reads the CSV file and stores the processed data in-memory."""
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                self.data = [row for row in csv_reader]
                # TODO: load and process csv
        except FileNotFoundError:
            print(f"File {self.file_path} not found.", flush=True)
            raise FileNotFoundError(f"CSV file not found: {self.file_path}")