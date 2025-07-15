# [miniml-rag](https://github.com/sealablab/miniml-rag)
# 🧠 Minimal RAG Pipeline with Qdrant

This project is a minimal, easy-to-understand Retrieval-Augmented Generation (RAG) pipeline written in Python 3.12.

It uses:
- 🧾 [`PyPDF2`](https://pypi.org/project/pypdf2/) for PDF parsing
- 🧬 [`Qdrant`](https://qdrant.tech) as the vector database
- ⚙️ [`httpx`](https://www.python-httpx.org/) for HTTP calls
- 🔧 [`pydantic`](https://docs.pydantic.dev/) for data models
- 📦 [`uv`](https://github.com/astral-sh/uv) for Python dependency management

---

## 🚀 Getting Started

### 1. Clone the repo and init submodules

```bash
git clone --recurse-submodules https://github.com/yourname/your-repo.git
cd your-repo
```

### 2. Create virtual environment and install deps

```bash
uv venv
uv pip install -e .
```

### 3. Start Qdrant and the Web UI

```bash
docker compose up --build
```

- Qdrant API: http://localhost:6333
- Qdrant Web UI: http://localhost:8686

---

## 🧪 Run the Example

```bash
python main.py
```

- This ingests a sample PDF (edit `main.py` to change the file)
- Then it runs a test search against the embedded chunks

---

## 🐟 Developer TMUX Session

Start a preconfigured dev shell with:

```bash
./tmux-rag-session.fish
```

- Top pane: Docker logs
- Bottom pane: Your CLI with venv activated

---

## 📁 Project Structure

```text
rag_pipeline/         ← Main Python package
├── ingest.py         ← PDF parsing + vectorization + Qdrant upload
├── query.py          ← Vector search interface
├── models.py         ← Shared pydantic models

qdrant-web-ui/        ← Qdrant dashboard (submodule)
qdrant-web-ui.Dockerfile ← Custom Dockerfile to build Web UI
```

---

## ⚙️ Config

Ports are defined in `.env`:

```env
QDRANT_PORT=6333
QDRANT_UI_PORT=8686
```

---

## 🙋‍♀️ Why This Exists

This is designed as a **reference implementation**: minimal, readable, and not bloated with frameworks. Ideal for learning or rapid prototyping.

---

## ✅ TODOs / Ideas

- Swap out dummy `vectorize()` with a real embedding model (OpenAI, HuggingFace, etc.)
- Add API (FastAPI)
- Add notebook for interactive demos
- CLI tool to inspect vector database

---

## 📝 License

MIT License
```



