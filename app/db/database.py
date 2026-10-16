from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession
from sqlalchemy import text, make_url
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

engineLocal: AsyncEngine = create_async_engine(
    url="postgresql+asyncpg://postgres:abc123%23@localhost:5432/NSE_DB",
    echo=False,
    pool_pre_ping=True
)

sessionLocal: AsyncSession = async_sessionmaker(
    bind=engineLocal,
    pool_size=20,
    max_overflow=20,
    pool_timeout=30,
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
        finally:
            logger.info("Closing db session")
            session.close()
