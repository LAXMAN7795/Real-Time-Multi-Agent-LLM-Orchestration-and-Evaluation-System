from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def generate_embedding(text: str):

    embedding = embedding_model.encode(text)

    return embedding.tolist()