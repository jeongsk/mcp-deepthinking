from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=[".env"], extra="ignore")

    api_key: Optional[str] = Field(default=...)
    provider: str = Field(default="groq")
    model_id: str = Field(default="deepseek-r1-distill-llama-70b")


settings = Settings()
