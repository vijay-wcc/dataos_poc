import asyncio
from fastapi import FastAPI
import logging
import sys

from app.process.main import worker
from app.routers.hello import hello_router
from app.routers.noise import noise_router
from app.routers.ai import ai_router
from app.utils.logger_config import setup_logger

setup_logger()

app = FastAPI()

app.include_router(hello_router)
app.include_router(noise_router)
app.include_router(ai_router)

logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_event():
    logger.info('API is starting up')
    loop = asyncio.get_running_loop()
    loop.create_task(start_worker())


@app.on_event("shutdown")
async def shutdown():
    logger.info('API is shutting down')
    await worker.stop()


async def start_worker():
    await worker.work()
