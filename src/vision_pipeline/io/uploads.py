from datetime import datetime
from pathlib import Path
import shutil

from fastapi import UploadFile

UPLOAD_DIR = Path("tmp/uploads")


def copy_local_image(image: Path) -> Path:

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Add _%f for microseconds if needed

    destination = (
        UPLOAD_DIR /
        f"{image.stem}_{timestamp}{image.suffix.lower()}"
    )

    shutil.copy2(image, destination)

    return destination


def save_uploaded_file(upload: UploadFile) -> Path:
    """
    Persist an uploaded image and return its local path.
    """

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    filename = Path(upload.filename)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # Add _%f for microseconds if needed

    destination = (
        UPLOAD_DIR /
        f"{filename.stem}_{timestamp}{filename.suffix.lower()}"
    )

    with destination.open("wb") as buffer:
        shutil.copyfileobj(upload.file, buffer)
    
    return destination