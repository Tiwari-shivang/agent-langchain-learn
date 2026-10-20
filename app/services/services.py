from app.db.database import get_db
from app.services.users import UserService
from app.services.agent import AgentService
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

def get_user_service(asyncSession: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(session=asyncSession)

def get_agent_service() -> AgentService:
    return AgentService()