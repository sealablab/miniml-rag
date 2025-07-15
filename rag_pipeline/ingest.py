from PyPDF2 import PdfReader
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams
import hashlib

def load_pdf_chunks(path: str, max_chars: int = 500) -> list[str]:
    reader = PdfReader(path)
    text = " ".join([page.extract_text() or "" for page in reader.pages])
    return [text[i:i + max_chars] for i in range(0, len(text), max_chars)]

def vectorize(text: str) -> list[float]:
    # Super dumb embedding
    return [ord(c) / 255.0 for c in text[:64]] + [0.0] * max(0, 64 - len(text))

def ingest_pdf(pdf_path: str, qdrant_url="http://localhost:6333"):
    chunks = load_pdf_chunks(pdf_path)
    client = QdrantClient(url=qdrant_url)

    collection = "rag_chunks"
    client.recreate_collection(
        collection_name=collection,
        vectors_config=VectorParams(size=64, distance="Cosine")
    )

    points = [
        PointStruct(
            id=int(hashlib.sha256(c.encode()).hexdigest(), 16) % (10**8),
            vector=vectorize(c),
            payload={"text": c}
        ) for c in chunks
    ]

    client.upsert(collection_name=collection, points=points)
