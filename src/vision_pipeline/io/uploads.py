from pathlib import Path
import shutil

from fastapi import UploadFile # HTTPException

from vision_pipeline.api.exceptions import bad_request

UPLOAD_DIR = Path("tmp/uploads")

def save_uploaded_file(upload: UploadFile) -> Path:
    """
    Persist an uploaded image and return its local path.
    """

    if not upload.content_type or not upload.content_type.startswith("image/"):
        # raise HTTPException(
        #     status_code=400,
        #     detail="Uploaded file must be an image."
        # )
        raise bad_request(f"Uploaded file must be an image.")

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    destination = UPLOAD_DIR / upload.filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload.file, buffer)

    return destination