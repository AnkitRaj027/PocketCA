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
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.
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

This process:

- Loads all PDFs
- Extracts text
- Splits documents into chunks
- Generates embeddings using Mistral
- Stores vectors in ChromaDB

---

## ▶️ Run the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

---

## 💬 Example Questions

- What is Section 80C?
- Explain Rule 3 of the Income-tax Rules.
- What are the deductions available under the old tax regime?
- What is TDS under Section 194J?
- Who is required to file an Income Tax Return?
- What are the provisions related to capital gains tax?

---

## ⚙️ How It Works

```text
Official PDF Documents
          │
          ▼
Document Loader
          │
          ▼
Text Splitter
          │
          ▼
Metadata Extraction
          │
          ▼
Mistral Embeddings
          │
          ▼
Chroma Vector Database
          │
          ▼
Semantic Retrieval
          │
          ▼
Prompt Construction
          │
          ▼
Mistral LLM
          │
          ▼
Answer with Source Citations
```

---

## ⚙️ Configuration

Application settings are managed through `.env` and `rag/settings.py`.

| Variable | Description |
|----------|-------------|
| `MISTRAL_API_KEY` | Mistral API key |
| `CHAT_MODEL` | Chat model name |
| `EMBEDDING_MODEL` | Embedding model name |
| `CHUNK_SIZE` | Size of each document chunk |
| `CHUNK_OVERLAP` | Overlap between consecutive chunks |
| `TOP_K` | Number of retrieved chunks |

---

## 📌 Current Capabilities

- Official PDF ingestion
- Automatic text chunking
- Metadata extraction
- Persistent vector database
- Semantic document retrieval
- Citation-supported responses
- Streamlit chat interface
- Mistral-powered RAG pipeline

---

## 🚧 Roadmap

Future improvements include:

- Hybrid Retrieval (Vector + BM25)
- Cross-Encoder Re-ranking
- User document uploads
- Form 16 analysis
- AIS statement analysis
- Income Tax Notice explanation
- Tax deduction recommendations
- ITR filing guidance
- Conversation memory
- Streaming responses
- Multi-document retrieval

---

## ⚠️ Disclaimer

PocketCA is intended for educational and informational purposes. While it retrieves information from official government documents, responses should not be considered professional legal or financial advice. Always verify important tax decisions using the latest government notifications or consult a qualified Chartered Accountant.

---

## 👨‍💻 Author

**Ankit Raj**

B.Tech in Artificial Intelligence & Machine Learning  
Lovely Professional University

---

If you found this project helpful, consider giving it a ⭐ on GitHub.
