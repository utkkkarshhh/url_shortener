from fastapi import FastAPI
from app.middlewares.cors import CORSMiddleware

from app.routes import urls
from app.views.home_view import home_router
from settings.dynamodb_config import setup_dynamodb

app = FastAPI()

app.add_middleware(CORSMiddleware)

setup_dynamodb()

app.include_router(home_router)
app.include_router(urls)
