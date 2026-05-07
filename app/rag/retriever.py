from app.rag.chroma_client import collection
from app.rag.embedding_service import generate_embedding


def retrieve_documents(
    query: str,
    top_k: int = 3
):

    query_embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    retrieved_chunks = []

    distances = results.get("distances")

    for idx, document in enumerate(results["documents"][0]):

        similarity_distance = (
            distances[0][idx]
            if distances
            else 0
        )

        retrieved_chunks.append({
            "chunk_id": results["ids"][0][idx],
            "content": document,
            "source": (
                results["metadatas"][0][idx]
                if results.get("metadatas")
                else {}
            ),
            "distance": similarity_distance
        })

    return retrieved_chunks