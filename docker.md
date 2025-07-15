# 🐳 Running Qdrant + Dashboard with Docker Compose

This project includes a `docker-compose.yml` file to launch both:

- 🧠 **Qdrant** (vector database on port `6333`)
- 🖥️ **Qdrant Web UI** (dashboard on port `8080`)

---

## 🚀 Quick Start

Make sure Docker and Docker Compose are installed. Then run:

``` bash
docker compose up
```
This will:
	• Start Qdrant on http://localhost:6333
	• Start the UI at http://localhost:8080


docker compose down

## 🛠️ Rebuild (if neededded)
docker compose build --no-cache


