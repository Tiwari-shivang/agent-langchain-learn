from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.users import UserCreateReq, UserDetails
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
    
    async def get_user_details(self, user_id: str) -> UserDetails | None:
        userRepo = UserRepository(session=self.session)
        try:
            response = await userRepo.get_user_details(user_id)
            userDetails = UserDetails(id=response.id, first_name=response.first_name, last_name=response.last_name, email=response.email, date_of_birth=response.date_of_birth, gender=response.gender, country=response.country, city=response.city)
            return userDetails
        except Exception as e:
            logger.error(f"Error while fetching details: {e.__cause__}")
            raise