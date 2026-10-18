from fastapi import APIRouter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

router = APIRouter()

@router.post("")
async def sign_up():
    logger.info("Route working")