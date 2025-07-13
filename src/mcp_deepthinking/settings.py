from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=[".env"], extra="ignore")

    api_key: str = Field(..., env="API_KEY")
    provider: str = Field("groq", env="PROVIDER")
    model_id: str = Field("deepseek-r1-distill-llama-70b", env="MODEL_ID")


settings = Settings()
