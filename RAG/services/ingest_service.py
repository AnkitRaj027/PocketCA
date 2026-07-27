

from pathlib import Path
from typing import List

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.config import OFFICIAL_DB, OFFICIAL_DOCS
from rag.logger import get_logger
from rag.models import models
from rag.schema import IngestionStats
from rag.settings import settings
from rag.utils.metadata import MetadataExtractor

logger = get_logger(__name__)


class IngestionService:
    

    def __init__(self) -> None:
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
        )

    def load_documents(self) -> List[Document]:
        

        documents: List[Document] = []

        pdf_files = list(Path(OFFICIAL_DOCS).glob("*.pdf"))

        if not pdf_files:
            logger.warning("No PDF files found in %s", OFFICIAL_DOCS)
            return documents

        for pdf in pdf_files:
            try:
                logger.info("Loading %s", pdf.name)

                loader = PyMuPDFLoader(str(pdf))
                documents.extend(loader.load())

            except Exception as exc:
                logger.exception(
                    "Failed to load %s : %s",
                    pdf.name,
                    exc,
                )

        return documents

    def split_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:
        

        logger.info("Splitting documents...")

        return self.splitter.split_documents(documents)

    def build_vector_database(
        self,
        chunks: List[Document],
    ) -> None:
        

        logger.info("Creating Chroma database...")

        Chroma.from_documents(
            documents=chunks,
            embedding=models.embedding_model,
            persist_directory=str(OFFICIAL_DB),
        )

        logger.info("Vector database created successfully.")

    def build_official_knowledge_base(
        self,
    ) -> IngestionStats:
        

        documents = self.load_documents()

        chunks = self.split_documents(documents)
        for chunk in chunks:
            metadata = MetadataExtractor.extract(chunk)

            chunk.metadata.update(metadata.model_dump())

        self.build_vector_database(chunks)

        stats = IngestionStats(
            documents=len(
                {
                    doc.metadata.get("source")
                    for doc in documents
                }
            ),
            pages=len(documents),
            chunks=len(chunks),
        )

        logger.info(stats.model_dump())

        return stats