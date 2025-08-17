from app.managers.get_user_urls_manager import GetUserURLsManager
from fastapi.responses import JSONResponse


class GetUserURLsView():
    def get(user_id: int):
        urls = GetUserURLsManager.get_user_urls(user_id)
        return JSONResponse(content={"urls": urls})
