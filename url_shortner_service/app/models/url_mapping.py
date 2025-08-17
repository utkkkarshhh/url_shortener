from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class URLMapping(BaseModel):
    long_url: str
    short_url: str
    expires_at: datetime
    created_at: datetime
    custom_alias: Optional[str] = None
    user_id: Optional[int] = None
    status: str = 'active'
    click_count: int = 0
