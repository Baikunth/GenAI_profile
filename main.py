# main.py
from fastapi import FastAPI, UploadFile, File
from services.rag_service import RAGService
from utils.file_handler import read_text_from_file
from pydantic import BaseModel
from typing import List

app = FastAPI()
rag_service = RAGService()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

@app.post("/ingest/")
async def ingest_document(file: UploadFile = File(...)):
    file_path = f"temp_files/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    text = read_text_from_file(file_path)
    if text:
        await rag_service.ingest(file.filename, text)
        return {"status": "Document ingested successfully"}
    return {"error": "Unsupported file type"}

@app.post("/query/")
async def query_documents(request: QueryRequest):
    results = await rag_service.retrieve(request.query, request.top_k)
    return {"results": results}
