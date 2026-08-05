import pytest
from pydantic import ValidationError

from vision_pipeline.api.exceptions import bad_request, internal_error, not_found
from vision_pipeline.api.responses import error_response, success_response
from vision_pipeline.api.schemas import APIResponse, InferenceRequest


def test_api_response_creation():
    response = APIResponse(
        status="success",
        message="OK",
        data={"output_directory": "outputs/predict/image.jpg"},
    )
    assert response.status == "success"
    assert response.message == "OK"
    assert response.data == {"output_directory": "outputs/predict/image.jpg"}


def test_api_response_model_dump():
    response = APIResponse(
        status="success",
        message="OK",
        data={"output_directory": "outputs/predict/image.jpg"},
    )
    assert response.model_dump() == {
        "status": "success",
        "message": "OK",
        "data": {"output_directory": "outputs/predict/image.jpg"},
    }


def test_api_response_required_fields():
    response = APIResponse(status="success", message="OK")
    assert response.status == "success"
    assert response.message == "OK"
    assert response.data is None


def test_api_response_validation():
    with pytest.raises(ValidationError):
        APIResponse(status=True, message="OK")


def test_inference_request_creation():
    request = InferenceRequest(image="examples/images/dog.jpg")
    assert request.image == "examples/images/dog.jpg"


def test_inference_request_model_dump():
    request = InferenceRequest(image="examples/images/dog.jpg")
    assert request.model_dump() == {"image": "examples/images/dog.jpg"}


def test_inference_request_required_field():
    with pytest.raises(ValidationError):
        InferenceRequest()


def test_inference_request_validation():
    with pytest.raises(ValidationError):
        InferenceRequest(image=123)


def test_success_response():
    response = success_response(
        message="Inference completed successfully.",
        data={"output_directory": "outputs/predict/image.jpg"},
    )
    assert response == {
        "status": "success",
        "message": "Inference completed successfully.",
        "data": {"output_directory": "outputs/predict/image.jpg"},
    }


def test_error_response():
    response = error_response(message="Image not found.")
    assert response == {
        "status": "error",
        "message": "Image not found.",
        "data": None,
    }


def test_bad_request():
    exc = bad_request("Image path cannot be empty.")
    assert exc.status_code == 400
    assert exc.detail == "Image path cannot be empty."


def test_not_found():
    exc = not_found("Image not found: missing.jpg")
    assert exc.status_code == 404
    assert exc.detail == "Image not found: missing.jpg"


def test_internal_error():
    exc = internal_error("Internal server error.")
    assert exc.status_code == 500
    assert exc.detail == "Internal server error."
