from fastapi import APIRouter

from app.views import *

routes = [
    ("/Healthcheck", HealthCheck.get, ["GET"]),
    ("/CreateShortURL", CreateShortURLView.post, ["POST"]),
    ("/FetchLongURL/{unique_id}", FetchLongURLView.get, ["GET"]),
]

v1_router = APIRouter()

for path, endpoint, methods in routes:
    v1_router.add_api_route(path, endpoint, methods=methods)
