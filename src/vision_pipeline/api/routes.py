from fastapi import APIRouter
from vision_pipeline.api.schemas import InferenceRequest, InferenceResponse
from vision_pipeline.pipelines.inference import run_inference

router = APIRouter()

@router.get("/")
def health():
    return {
        "project": "Vision Pipeline",
        "status": "running",
    }

@router.post(
    "/predict",
    response_model=InferenceResponse
)
def inference(request: InferenceRequest):
    results = run_inference(request.image)

    return InferenceResponse(
        status="success",
        output=str(results[0].save_dir),
    )