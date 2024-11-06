# services/rag_service.py
from models.embeddings import EmbeddingModel
from services.db_service import ChromaDBClient

class RAGService:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.db_client = ChromaDBClient()

    async def ingest(self, doc_id: str, text: str):
        embedding = self.embedding_model.embed(text)
        metadata = {"document_id": doc_id, "content": text}
        self.db_client.ingest_document(doc_id, embedding, metadata)

    async def retrieve(self, query: str, top_k: int = 5):
        embedding = self.embedding_model.embed(query)
        return self.db_client.query(embedding, top_k=top_k)
