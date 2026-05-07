from pathlib import Path

from app.rag.chroma_client import collection
from app.rag.embedding_service import generate_embedding


DOCUMENT_PATH = "app/rag/documents/renewable_energy.txt"


def ingest_documents():

    file_content = Path(DOCUMENT_PATH).read_text()

    chunks = [
        chunk.strip()
        for chunk in file_content.split("\n")
        if chunk.strip()
    ]

    for idx, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"chunk_{idx}"]
        )

    print("Documents ingested successfully.")