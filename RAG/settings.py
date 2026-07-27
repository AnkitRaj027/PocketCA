from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    mistral_api_key: SecretStr

    chat_model: str = "mistral-medium-latest"
    embedding_model: str = "mistral-embed"

    chunk_size: int = 1000
    chunk_overlap: int = 200
    top_k: int = 8


settings = Settings()
