from app.managers import FetchLongURLManager
from fastapi.responses import JSONResponse


class FetchLongURLView():
    def get(unique_id: str):
        long_url = FetchLongURLManager.get_long_url(unique_id)
        return JSONResponse(content={"long_url": long_url})
