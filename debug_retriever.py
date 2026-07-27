import sys
from rag.services.retriever_service import RetrieverService

print("=" * 60)
print("RETRIEVER DEBUG")
print("=" * 60)

retriever = RetrieverService()

# Get all documents
all_docs = retriever.load_all_documents()
print(f"\nTotal documents in vector DB: {len(all_docs)}")

if len(all_docs) == 0:
    print("ERROR: Vector database is empty!")
    print("\nPlease run ingest to populate the database.")
    print("You need to rebuild the vector database with the documents.")
    sys.exit(1)

# Test a simple query
print("\n" + "=" * 60)
print("TEST QUERY: 'what is rule 1'")
print("=" * 60)

docs = retriever.retrieve('what is rule 1', k=5)
print(f"\nRetrieved {len(docs)} documents")

for i, doc in enumerate(docs):
    filename = doc.metadata.get("filename", "Unknown")
    page = doc.metadata.get("page", "Unknown")
    source = doc.metadata.get("source", "Unknown")
    print(f"\n--- Document {i+1} ---")
    print(f"Filename: {filename}")
    print(f"Page: {page}")
    print(f"Source: {source}")
    print(f"Content length: {len(doc.page_content)} chars")
    print(f"Content preview:\n{doc.page_content[:300]}")

# Test similarity search with scores
print("\n" + "=" * 60)
print("SIMILARITY SEARCH WITH SCORES")
print("=" * 60)

scored_docs = retriever.retrieve_with_scores('what is rule 1', k=5)
print(f"\nRetrieved {len(scored_docs)} documents with scores")

for i, (doc, score) in enumerate(scored_docs):
    filename = doc.metadata.get("filename", "Unknown")
    page = doc.metadata.get("page", "Unknown")
    print(f"Doc {i+1}: {filename} (Page {page}) - Score: {score:.4f}")
