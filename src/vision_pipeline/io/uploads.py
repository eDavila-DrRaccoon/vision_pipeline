from datetime import datetime
from pathlib import Path
import shutil

from fastapi import UploadFile # HTTPException

from vision_pipeline.api.exceptions import bad_request, not_found

UPLOAD_DIR = Path("tmp/uploads")
SUPPORTED_IMAGE_TYPES = {
    "image/jpg",
    "image/jpeg",
    "image/png",
    "image/bmp",
    "image/tif",
    "image/tiff",
    "image/webp"
}

def save_uploaded_file(upload: UploadFile) -> Path:
    """
    Persist an uploaded image and return its local path.
    """

    if not upload.content_type or not upload.content_type.startswith("image/"):
        # raise HTTPException(
        #     status_code=400,
        #     detail="Uploaded file must be an image."
        # )
        raise bad_request("Uploaded file must be an image.")

    if upload.content_type not in SUPPORTED_IMAGE_TYPES:
        raise bad_request("Unsupported image format. Supported formats: .jpg, .jpeg, .png, .bmp, .tif, .tiff, and .webp.")

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    filename = Path(upload.filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Add _%f for microseconds if needed
    destination = (UPLOAD_DIR / f"{filename.stem}_{timestamp}{filename.suffix}")

    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload.file, buffer)

    if not destination.exists():
        # raise HTTPException(
        #     status_code=404,
        #     detail=f"Image not found: {image}",
        # )
        raise not_found(f"Image not found: {destination}")

    return destination