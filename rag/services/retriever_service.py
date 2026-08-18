
from typing import List, Optional

from langchain_core.documents import Document
from langchain_chroma import Chroma

from rag.config import OFFICIAL_DB
from rag.models import models
from rag.settings import settings


class RetrieverService:
    
    def __init__(self) -> None:

        self.vector_store = Chroma(
            persist_directory=str(OFFICIAL_DB),
            embedding_function=models.embedding_model,
        )

    def retrieve(
        self,
        query: str,
        k: int = settings.top_k,
        filter: Optional[dict] = None,
    ) -> List[Document]:
        

        search_kwargs = {"k": k}
        if filter is not None:
            search_kwargs["filter"] = filter

        retriever = self.vector_store.as_retriever(search_kwargs=search_kwargs)

        return retriever.invoke(query)
    def retrieve_with_scores(
    self,
    query: str,
    k: int = 5,
    ):
        

        return self.vector_store.similarity_search_with_score(
            query=query,
            k=k,
        )

    def load_all_documents(self) -> List[Document]:
        
        try:
            res = self.vector_store.get()
            if not res or "documents" not in res:
                return []
            
            documents = []
            for text, meta in zip(res.get("documents", []), res.get("metadatas", [])):
                documents.append(Document(page_content=text, metadata=meta))
            return documents
        except Exception:
            return []
