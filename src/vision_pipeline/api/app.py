from fastapi import FastAPI

from vision_pipeline.api.handlers import register_exception_handlers
from vision_pipeline.api.routes import router

app = FastAPI(
    title="Vision Pipeline",
    version="0.1.0",
)

app.include_router(router)

register_exception_handlers(app)