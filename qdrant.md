# 🧠 Running Qdrant Locally

Qdrant is the vector database used by this project to store and search embeddings.  
To run it locally (default: port **6333**), follow one of the methods below:

---

## 🚀 Option 1: Run with Docker (recommended)

Make sure you have Docker installed.

```bash
docker run -p 6333:6333 qdrant/qdrant
```



## 🧪 Verify It’s Running

```
curl http://localhost:6333/health
docker ps
```

## Stopping qdrant (docker)
```
docker stop <id>
```


