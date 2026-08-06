from typing import Any
from pydantic import BaseModel, ConfigDict

class InferenceRequest(BaseModel):
    image: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "image": "examples/images/dog_and_person.jpg"
            }
        }
    )

class APIResponse(BaseModel):
    status: str
    message: str
    data: Any = None