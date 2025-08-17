import os
from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str = Field(..., alias="AWS_DEFAULT_REGION")
    dynamodb_endpoint_url: Optional[str] = None

    class Config:
        env_file = "/app/.env"


@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
