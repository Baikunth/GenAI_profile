# services/db_service.py
import chromadb
from chromadb.config import Settings
from chromadb.utils import Metadata, SearchResults

class ChromaDBClient:
    def __init__(self):
        self.client = chromadb.Client(Settings(persist_directory="chromadb_data"))
        self.collection = self.client.get_or_create_collection("documents")

    def ingest_document(self, doc_id: str, embedding: list, metadata: Metadata):
        self.collection.add(doc_id, embedding, metadata)

    def query(self, embedding: list, top_k: int = 5) -> SearchResults:
        return self.collection.query(embedding, top_k=top_k)
