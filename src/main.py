from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from src.settings import settings
from src.api import api_routes

import os

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

origins = ["*"]

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
]

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_DESCRIPTION,
    middleware=middleware,
)

app.include_router(api_routes)
