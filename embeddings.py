# models/embeddings.py
from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    def embed(self, text: str):
        return self.model.encode(text, show_progress_bar=False)
