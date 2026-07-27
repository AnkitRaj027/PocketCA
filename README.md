# PocketCA

PocketCA is a Streamlit-based AI assistant for Indian tax and accounting questions. It uses a retrieval-augmented generation workflow: user questions are matched against an official PDF knowledge base stored in Chroma, then answered with Mistral models through LangChain.

## Features

- Chat interface built with Streamlit.
- Retrieval over official documents with source citations.
- Mistral chat and embedding models.
- Persistent vector storage for the official knowledge base.
- Simple document ingestion pipeline for PDF sources.

## Requirements

- Python 3.10 or newer.
- A valid Mistral API key.
- Official PDF documents placed in `data/official_docs/`.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

3. Create a `.env` file in the project root with your API key:

	```env
	mistral_api_key=your_mistral_api_key_here
	```

## Run the app

Start the Streamlit app with:

```bash
streamlit run app.py
```

## Rebuild the knowledge base

The ingestion pipeline lives in `rag/services/ingest_service.py`. To rebuild the official vector database after adding or updating PDFs in `data/official_docs/`, run the following in a Python shell:

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
