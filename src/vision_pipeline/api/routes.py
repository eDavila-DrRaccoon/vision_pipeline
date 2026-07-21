from typing import Annotated
from fastapi import APIRouter, Body
from vision_pipeline.api.responses import success_response
from vision_pipeline.api.schemas import InferenceRequest, APIResponse
from vision_pipeline.pipelines.inference import run_inference

router = APIRouter()

## Health Check
@router.get("/",
            response_model=APIResponse,
            summary="Health check",
            description="Check if the Vision Pipeline API is running.",
            tags=["Health"]
            )
def health():
    return success_response(
        message="Vision Pipeline API is running." 
    )

## Inference Endpoint 
@router.post("/inference",
            response_model=APIResponse,
            summary="Run image inference",
            description="Runs YOLO11 inference on a local image.",
            tags=["Inference"]
            )
def inference(request: Annotated[InferenceRequest,
                                Body(example={
                                        "image": "examples/images/dog_and_person.jpg"
                                        }
                                    ),
                                ]
            ):

    results = run_inference(request.image)

    return success_response(
        message="Inference completed successfully.",
        data={
            "output_directory": str(results[0].save_dir)
        },
    )