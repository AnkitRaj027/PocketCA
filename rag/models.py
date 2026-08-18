

from langchain_mistralai import ChatMistralAI
from langchain_mistralai import MistralAIEmbeddings

from rag.settings import settings


class ModelManager:
    

    def __init__(self) -> None:

        self.chat_llm = ChatMistralAI(
            api_key=settings.mistral_api_key.get_secret_value(),
            model=settings.chat_model,
            temperature=0,
        )

        self.embedding_model = MistralAIEmbeddings(
            api_key=settings.mistral_api_key.get_secret_value(),
            model=settings.embedding_model,
        )


models = ModelManager()