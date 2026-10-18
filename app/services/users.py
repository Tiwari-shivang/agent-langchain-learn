from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.users import UserCreateReq
from app.repositories.users import UserRepository
from app.schemas.users import SuccessResponse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def sign_up(self, request: UserCreateReq) -> SuccessResponse:
        userRepo = UserRepository(session=self.session)
        try:
            await userRepo.create_user(request)
            response = SuccessResponse(message="User created successfully")
        except Exception as e:
            logger.error(f"Error signing up: {e.__cause__}")
            raise
        return response
