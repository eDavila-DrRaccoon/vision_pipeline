from fastapi import FastAPI

from vision_pipeline.api.routes import router

app = FastAPI(
    title="Vision Pipeline",
    version="0.1.0",
)

app.include_router(router)