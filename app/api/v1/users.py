from fastapi import APIRouter, Depends
from app.services.services import get_user_service
from app.services.users import UserService
from app.schemas.users import UserCreateReq, SuccessResponse, UserDetails
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

router = APIRouter()

@router.post("")
async def sign_up(request: UserCreateReq, userService: UserService = Depends(get_user_service)) -> SuccessResponse:
    response = await userService.sign_up(request=request)
    return response

@router.get("/{user_id}")
async def user_details(user_id: str, userService: UserService = Depends(get_user_service)) -> UserDetails:
    response = await userService.get_user_details(user_id)
    return response