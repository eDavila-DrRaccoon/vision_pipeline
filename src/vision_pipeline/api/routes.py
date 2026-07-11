from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health():
    return {
        "project": "Vision Pipeline",
        "status": "running",
    }