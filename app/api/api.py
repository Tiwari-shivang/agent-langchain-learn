from fastapi import APIRouter
from app.api.v1.health import router as health_router
from app.api.v1.agent import router as agent_router

router = APIRouter()

router.include_router(health_router, prefix="/health")
router.include_router(agent_router, prefix="/agent")