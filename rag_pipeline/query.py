from qdrant_client import QdrantClient
from rag_pipeline.ingest import vectorize

def search(query: str, top_k=3, qdrant_url="http://localhost:6333"):
    vec = vectorize(query)
    client = QdrantClient(url=qdrant_url)
    results = client.search(collection_name="rag_chunks", query_vector=vec, limit=top_k)
    return [r.payload["text"] for r in results]
