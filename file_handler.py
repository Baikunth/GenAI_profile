# utils/file_handler.py
import fitz  # PyMuPDF for PDFs
from docx import Document
from typing import Optional
import os

def read_text_from_file(file_path: str) -> Optional[str]:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = ""
        with fitz.open(file_path) as pdf:
            for page in pdf:
                text += page.get_text()
        return text
    elif ext == ".docx":
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return None
