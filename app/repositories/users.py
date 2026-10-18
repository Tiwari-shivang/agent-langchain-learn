from app.repositories.baseRepository import BaseRepository
from app.db.models import Users
from app.schemas.users import UserCreateReq
import logging
import bcrypt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserRepository(BaseRepository[Users]):
    async def create_user(self, userData: UserCreateReq):
        encoded_pass = userData.password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(encoded_pass, salt)
        hashed_password = hashed_bytes.decode("utf-8")
        new_user: Users = Users(
            first_name = userData.first_name,
            last_name = userData.last_name,
            email = userData.email,
            password_hash = hashed_password,
            date_of_birth = userData.date_of_birth,
            gender = userData.gender,
            country = userData.country,
            city = userData.city,
            )
        try:
            self.session.add(new_user)
            await self.session.commit()
            await self.session.refresh(new_user)
            logger.info(f"user data: {new_user}")
        except Exception as e:
            self.session.rollback()
            logger.error(f"Error creating user: {e.__cause__}")
        return
        