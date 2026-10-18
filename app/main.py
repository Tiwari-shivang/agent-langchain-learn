from fastapi import FastAPI
from app.api.api import router
from contextlib import asynccontextmanager
from app.db.database import test_db_connection, engineLocal, get_db
from app.db.base import Base
from app.db import models  # Register model tables before create_all runs.
from sqlalchemy.schema import CreateSchema
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def life_span(app: FastAPI):
    try:
        await test_db_connection()
        async with engineLocal.begin() as engine:
            for schema in sorted({table.schema for table in Base.metadata.tables.values() if table.schema}):
                await engine.execute(CreateSchema(schema, if_not_exists=True))
            await engine.run_sync(Base.metadata.create_all)
        session = get_db()
        app.state.session = session
        yield
    except Exception:
        logger.exception("Application lifespan failed")
        raise
    finally:
        logger.info("Application shutting down!")
        await engineLocal.dispose()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=life_span)
    app.include_router(router)
    return app

app = create_app()
