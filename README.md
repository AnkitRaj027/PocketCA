# PocketCA 💼🇮🇳

PocketCA is an AI-powered tax assistant designed to simplify access to official Indian tax information. Built using Retrieval-Augmented Generation (RAG), it retrieves relevant content from official government documents before generating responses, ensuring answers are grounded in trusted sources rather than relying solely on a language model.

The application leverages **Mistral AI**, **LangChain**, **ChromaDB**, and **Streamlit** to provide a fast, citation-backed conversational experience for tax-related queries.

---

## ✨ Features

- 🤖 AI-powered conversational tax assistant
- 📄 Chat with official Indian tax documents
- 🔍 Semantic document retrieval using ChromaDB
- 📚 Retrieval-Augmented Generation (RAG) pipeline
- 🧠 Mistral AI for chat completion and embeddings
- 📑 Automatic PDF ingestion and text chunking
- 📌 Source citations with document and page references
- 💾 Persistent vector database for official documents
- 🖥️ Clean and interactive Streamlit interface
- 🏗️ Modular architecture for future enhancements

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Mistral AI
- ChromaDB
- PyMuPDF
- Pydantic
- Python Dotenv

---

## 📁 Project Structure

```text
PocketCA/
│
├── app.py
├── data/
│   ├── official_docs/
│   └── user_uploads/
│
├── rag/
│   ├── services/
│   ├── prompts/
│   ├── utils/
│   ├── config.py
│   ├── settings.py
│   ├── models.py
│   ├── schema.py
│   └── logger.py
│
├── storage/
│   ├── official_db/
│   └── session_db/
│
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/PocketCA.git
cd PocketCA
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key

CHAT_MODEL=mistral-small-latest
EMBEDDING_MODEL=mistral-embed

CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K=5
```

---

## 📂 Add Official Documents

Place all official government PDF documents inside:

```text
data/
└── official_docs/
```

Example:

```text
official_docs/
├── Income-tax-Rules-2026.pdf
├── Finance-Act-2026.pdf
├── CBDT-Circular.pdf
└── GST-Manual.pdf
```

---

## 🧠 Build the Knowledge Base

After adding your PDF documents, generate embeddings and create the vector database.

```python
from rag.services.ingest_service import IngestionService

IngestionService().build_official_knowledge_base()
```

This will read the PDFs, split them into chunks, extract metadata, and write the Chroma database to `storage/official_db/`.


## Configuration

Key settings are loaded from `.env` and `rag/settings.py`:

- `mistral_api_key` - required.
- `chat_model` - defaults to `mistral-medium-latest`.
- `embedding_model` - defaults to `mistral-embed`.
- `chunk_size`, `chunk_overlap`, `top_k` - retrieval and chunking defaults.

## Notes

- Answers only include citations when retrieved documents are relevant enough.
- If the assistant cannot find a relevant answer in the official knowledge base, it falls back to a default refusal message.
