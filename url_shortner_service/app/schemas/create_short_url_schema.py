from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateShortURLRequestSchema(BaseModel):
    long_url: str
    expiration_date: datetime
    custom_alias: Optional[str] = None
    user_id: int


class CreateShortURLResponseSchema(BaseModel):
    short_url: str
    long_url: str
    created_at: datetime
    expiration_date: datetime
