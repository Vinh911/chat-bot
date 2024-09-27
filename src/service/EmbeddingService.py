from sentence_transformers import SentenceTransformer

class EmbeddingService:
    """
    This service is responsible for generating embeddings using
    the sentence_transformers model.
    """

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.model = None

    def load_model(self):
        """Loads the SentenceTransformer model specified by the model_name."""
        print(f"Loading embedding model: {self.model_name}...", flush=True)

        # TODO: handle exception if model is not found
        self.model = SentenceTransformer(self.model_name)
        
        print(f"Embedding model '{self.model_name}' loaded successfully.", flush=True)