import chromadb


client = chromadb.PersistentClient(path="./chromadb_data")

collection = client.get_or_create_collection(
    name="knowledge_base"
)