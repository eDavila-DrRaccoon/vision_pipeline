from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Body, File, HTTPException, UploadFile

from vision_pipeline.api.schemas import APIResponse, InferenceRequest
from vision_pipeline.api.responses import success_response
from vision_pipeline.api.exceptions import bad_request, not_found, internal_error
from vision_pipeline.io.uploads import save_uploaded_file
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

## Local Inference Endpoint 
@router.post(
    "/inference/local",
    response_model=APIResponse,
    summary="Run image inference from local file",
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
        raise bad_request("Image path cannot be empty.")

    if not image.exists():
        # raise HTTPException(
        #     status_code=404,
        #     detail=f"Image not found: {image}",
        # )
        raise not_found(f"Image not found: {request.image}")

    try:
        # a) results (results[0].save_dir) for the original save dir,
        # b) output for the new location
        output = run_inference(request.image)

        return success_response(
            message="Inference completed successfully.",
            data={
                "output_directory": str(output)
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

## Upload and Inference Endpoint
@router.post(
    "/inference/upload",
    response_model=APIResponse,
    summary="Run image inference from uploaded file",
    description="Runs YOLO11 inference on an uploaded image.",
    tags=["Inference"],
    responses={
        400: {"description": "Invalid request"},
        404: {"description": "Image not found"},
        500: {"description": "Internal server error"},
    },
)
async def inference_upload(
    image: UploadFile = File(...,
        description=(
            "Image file to process."
        )
    )
):
    
    try:
        # Persist the uploaded image and get its local path
        # Inside of Try block in case of any unexpected errors, e.g., file system issues, permission errors, full disk, etc.
        image_path = save_uploaded_file(image)

        output = run_inference(image_path)

        return success_response(
            message="Inference completed successfully.",
            data={
                "output_directory": str(output)
            },
        )

    except HTTPException:
        raise

    except Exception as exc:
        raise internal_error(f"Internal server error: {str(exc)}")