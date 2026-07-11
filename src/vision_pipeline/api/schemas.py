from pydantic import BaseModel

class InferenceRequest(BaseModel):
    image: str

class InferenceResponse(BaseModel):
    status: str
    output: str