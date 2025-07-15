from rag_pipeline.ingest import ingest_pdf
from rag_pipeline.query import search

if __name__ == "__main__":
    ingest_pdf("example.pdf")  # Your PDF goes here
    results = search("Tell me about the policy")
    print("Top Matches:")
    for r in results:
        print("-", r[:200], "...")
