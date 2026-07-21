from typing import Any
from pydantic import BaseModel

class InferenceRequest(BaseModel):
    image: str

class APIResponse(BaseModel):
    status: str
    message: str
    data: Any = None