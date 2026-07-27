

from pathlib import Path

from langchain_core.documents import Document

from rag.schema import PDFMetadata


class MetadataExtractor:
   

    @staticmethod
    def extract(document: Document) -> PDFMetadata:
       

        source = Path(
            document.metadata.get("source", "")
        )

        filename = source.name

        return PDFMetadata(
            filename=filename,
            filepath=str(source),
            category=MetadataExtractor.detect_category(filename),
            page=document.metadata.get("page", 0) + 1,
        )

    @staticmethod
    def detect_category(filename: str) -> str:
        

        name = filename.lower()

        if "gst" in name:
            return "GST"

        if "income" in name or "tax" in name:
            return "Income Tax"

        if "epfo" in name:
            return "EPFO"

        if "tds" in name:
            return "TDS"

        return "General"