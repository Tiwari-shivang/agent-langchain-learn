from fastapi import APIRouter

router = APIRouter()

@router.get("")
def health_check():
    return "Application is up and working"