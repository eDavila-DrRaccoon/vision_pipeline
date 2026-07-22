from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Body, HTTPException

from vision_pipeline.api.schemas import APIResponse, InferenceRequest
from vision_pipeline.api.responses import success_response
from vision_pipeline.api.exceptions import bad_request, not_found, internal_error
from vision_pipeline.pipelines.inference import run_inference

router = APIRouter()

## Health Check
@router.get(
    "/",
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
@router.post(
    "/inference",
    response_model=APIResponse,
    summary="Run image inference",
    description="Runs YOLO11 inference on a local image.",
    tags=["Inference"],
    responses={
        400: {"description": "Invalid request"},
        404: {"description": "Image not found"},
        500: {"description": "Internal server error"},
    },
)
def inference(
    request: Annotated[
        InferenceRequest,
        Body(
            example={
                "image": "examples/images/dog_and_person.jpg"
            }
        ),
    ]
):

    image = Path(request.image)

    if not request.image.strip():
        # raise HTTPException(
        #     status_code=400,
        #     detail="Image path cannot be empty.",
        # )
        raise bad_request(f"Image path cannot be empty.")

    if not image.exists():
        # raise HTTPException(
        #     status_code=404,
        #     detail=f"Image not found: {image}",
        # )
        raise not_found(f"Image not found: {request.image}")

    try:
        # a) results (results[0].save_dir) for the original save dir,
        # b) final_output for the new location
        final_output = run_inference(request.image)

        return success_response(
            message="Inference completed successfully.",
            data={
                "output_directory": final_output
            },
        )

    except HTTPException:
        raise

    except Exception as exc:
        # raise HTTPException(
        #     status_code=500,
        #     detail=str(exc),
        # )
        raise internal_error(f"Internal server error: {str(exc)}")