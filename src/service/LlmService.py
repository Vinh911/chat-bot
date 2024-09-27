from gpt4all import GPT4All

class LlmService:
    """
    The service is responsible for generating responses using a local
    SentenceTransformer model based on the input data.
    """

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = None

    def load_model(self):
        print(f"Loading Llm model: {self.model_name}...", flush=True)
        self.model = GPT4All(self.model_name) # downloads / loads a 4.66GB LLM

    def generate_prompt(self, message: str):
        return self.model.generate(message, max_tokens=200)