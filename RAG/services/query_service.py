"""
Query orchestration service.
"""

from langchain_core.messages import HumanMessage, SystemMessage
from pathlib import Path

from rag.services.retriever_service import RetrieverService
from rag.models import models
from rag.schema import QueryResponse, SourceReference
from rag.settings import settings

from rag.prompt_manager import PromptManager


SYSTEM_PROMPT = PromptManager.load(
    "system_prompt.txt"
)

FALLBACK_MESSAGE = "I couldn't find this information in the official knowledge base."
# Similarity score threshold below which results are not considered relevant
RELEVANCE_THRESHOLD = 0.5


class QueryService:

    def __init__(self):
        # A single vector retriever keeps the search path predictable and
        # avoids combining unrelated keyword and semantic results.
        self.retriever = RetrieverService()

    @staticmethod
    def _sources_for(docs) -> list[SourceReference]:
        """Build display citations without changing the retrieval result."""
        sources = []
        seen_sources = set()

        for doc in docs:
            filename = doc.metadata.get("filename")
            page = doc.metadata.get("page")

            if not filename:
                source_path = doc.metadata.get("source") or doc.metadata.get("file_path")
                filename = Path(source_path).name if source_path else "Unknown"
                # Loader metadata is zero-indexed when no normalized metadata
                # was stored during ingestion.
                page = (page + 1) if page is not None else 1
            elif page is None:
                page = 1

            source_key = (filename, page)
            if source_key not in seen_sources:
                seen_sources.add(source_key)
                sources.append(SourceReference(filename=filename, page=page))

        return sources

    @staticmethod
    def _messages(question: str, docs):
        context = "\n\n---\n\n".join(doc.page_content for doc in docs)
        return [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=f"""Context:\n\n{context}\n\nQuestion:\n\n{question}""",
            ),
        ]

    def ask(
        self,
        question: str,
    ) -> QueryResponse:

        # Get documents with similarity scores
        docs_with_scores = self.retriever.retrieve_with_scores(question, k=settings.top_k)
        
        # Check if top result meets relevance threshold
        is_relevant = False
        if docs_with_scores:
            top_score = docs_with_scores[0][1]
            is_relevant = top_score >= RELEVANCE_THRESHOLD
        
        # Only use docs if they're above threshold
        docs = [doc for doc, score in docs_with_scores]
        
        messages = self._messages(question, docs)
        response = models.chat_llm.invoke(messages)
        
        # Only return sources if:
        # 1. The LLM didn't return the fallback message AND
        # 2. The retrieval results were above the relevance threshold
        sources = []
        if is_relevant and FALLBACK_MESSAGE not in response.content:
            sources = self._sources_for(docs)

        return QueryResponse(
            answer=response.content,
            sources=sources,
        )

    def ask_stream(self, question: str):
        """
        Ask a question and return a generator and sources tuple.
        Sources are determined after streaming completes based on whether
        the response contains the fallback message.
        
        Returns:
            tuple: (generator, sources_list)
            The sources_list will be populated/updated after the generator completes.
        """
        docs = self.retriever.retrieve(question, k=settings.top_k)
        messages = self._messages(question, docs)

        # Create a container to hold the response and share it with the generator
        response_container = {'content': '', 'sources': None}
        
        def response_generator():
            for chunk in models.chat_llm.stream(messages):
                content = chunk.content
                response_container['content'] += content
                yield content
            
            # After all chunks are streamed, determine if we should show sources
            if FALLBACK_MESSAGE not in response_container['content']:
                response_container['sources'] = self._sources_for(docs)
            else:
                response_container['sources'] = []

        return response_generator(), response_container
