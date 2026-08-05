from pathlib import Path

from fastapi import UploadFile # HTTPException

from vision_pipeline.api.exceptions import bad_request, not_found

SUPPORTED_IMAGE_SUFFIXES = {
    ".avif",
    ".bmp",
    ".dng",
    ".heic",
    ".heif",
    ".jp2",
    ".jpeg",
    ".jpg",
    ".mpo",
    ".png",
    ".tif",
    ".tiff",
    ".webp",
}

SUPPORTED_IMAGE_TYPES = {
    "image/avif",
    "image/bmp",
    "image/dng",
    "image/heic",
    "image/heif",
    "image/jp2",
    "image/jpeg",
    "image/jpg",
    "image/mpo",
    "image/png",
    "image/tif",
    "image/tiff",
    "image/webp",
}


def _supported_formats() -> str:
    return ", ".join(sorted(SUPPORTED_IMAGE_SUFFIXES))


def validate_image_path(image: Path) -> None:
    """
    Validate an image referenced by a filesystem path.
    """

    if not image.exists():
        # raise HTTPException(
        #     status_code=404,
        #     detail=f"Image not found: {image}",
        # )
        raise not_found(f"Image not found: {image}")

    if image.suffix.lower() not in SUPPORTED_IMAGE_SUFFIXES:
        raise bad_request(f"Unsupported image format. Supported formats: {_supported_formats()}.")


def validate_uploaded_image(upload: UploadFile) -> None:
    """
    Validate an uploaded image.
    """

    if not upload.content_type or not upload.content_type.startswith("image/"):
        # raise HTTPException(
        #     status_code=400,
        #     detail="Uploaded file must be an image."
        # )
        raise bad_request("Uploaded file must be an image.")

    filename = Path(upload.filename or "")

    if filename.suffix.lower() not in SUPPORTED_IMAGE_SUFFIXES:
        raise bad_request(
            f"Unsupported image format. Supported formats: {_supported_formats()}."
        )

    if upload.content_type in SUPPORTED_IMAGE_TYPES or upload.content_type == "application/octet-stream":
        return

    raise bad_request(f"Unsupported image MIME type: {upload.content_type}.")