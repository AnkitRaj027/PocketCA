from rag.services.retriever_service import RetrieverService

retriever = RetrieverService()

documents = retriever.retrieve(
    "What is Section 80C?"
)

for doc in documents:
    print(doc.page_content)