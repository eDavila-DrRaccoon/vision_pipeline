from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from vision_pipeline.api.responses import error_response

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException,
    ):

        return JSONResponse(
            status_code=exc.status_code,
            content=error_response(exc.detail),
        )