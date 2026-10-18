from fastapi import APIRouter, Depends
from app.services.services import get_user_service
from app.services.users import UserService
from app.schemas.users import UserCreateReq, SuccessResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

router = APIRouter()

@router.post("")
async def sign_up(request: UserCreateReq, userService: UserService = Depends(get_user_service)) -> SuccessResponse:
    response = await userService.sign_up(request=request)
    return response