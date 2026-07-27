from rag.services.query_service import QueryService

query = QueryService()

response = query.ask(
    "What is Section 80C?"
)

print(response.answer)

print(response.sources)