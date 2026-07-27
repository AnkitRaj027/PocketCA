from rag.services.ingest_service import IngestionService

service = IngestionService()

stats = service.build_official_knowledge_base()

print(stats)