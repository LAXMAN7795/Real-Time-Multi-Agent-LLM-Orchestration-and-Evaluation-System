from fastapi import APIRouter

from app.rag.ingest import ingest_documents


router = APIRouter()


@router.post("/ingest-documents")

async def ingest_route():

    ingest_documents()

    return {
        "status": "documents_ingested"
    }