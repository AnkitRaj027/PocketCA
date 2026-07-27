from pathlib import Path
from typing import Optional
from typing import List

from pydantic import BaseModel, Field


class PDFMetadata(BaseModel):
    filename: str
    filepath: str
    category: str
    page: int
    title: str | None = None
    authority: str | None = None
    document_type: str | None = None
    year: int | None = None


class IngestionStats(BaseModel):
    documents: int = Field(default=0, ge=0)
    pages: int = Field(default=0, ge=0)
    chunks: int = Field(default=0, ge=0)


class RetrievalResult(BaseModel):
    content: str
    source: str
    page: int
    score: float


class Citation(BaseModel):
    source: str
    page: int


class RetrievedChunk(BaseModel):
    content: str
    source: str
    page: int
    score: float

class SourceReference(BaseModel):
    filename: str
    page: int


class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceReference]
class ChatMessage(BaseModel):
    role: str
    content: str