from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession
from sqlalchemy import text, make_url
from app.core.settings import get_settings
import logging

settings = get_settings()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engineLocal: AsyncEngine = create_async_engine(
    url=f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
    echo=False,
    pool_size=20,
    max_overflow=20,
    pool_timeout=20,
    pool_pre_ping=True
)

sessionLocal: AsyncSession = async_sessionmaker(
    bind=engineLocal,
    autoflush=False,
    expire_on_commit=False
)

async def test_db_connection():
    async with engineLocal.connect() as conn:
        try:
            await conn.execute(text("SELECT 1"))
            logger.info("DB connected successfully")
        except Exception as e:
            logger.error(f"Error connecting DB: {e.__cause__}")
            raise

async def get_db():
    async with sessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            logger.error(f"Error in db session {e.__cause__}")
            await session.rollback()
            raise
        finally:
            logger.info("Closing db session")
            await session.close()
