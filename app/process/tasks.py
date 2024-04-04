import logging

from pyzeebe import ZeebeTaskRouter

from app.schema.location import Location

simple_tasks_router = ZeebeTaskRouter()

logger = logging.getLogger(__name__)


@simple_tasks_router.task(task_type="my_task")
async def my_task(category: str, description: str, location: Location):
    logger.info("Category: %s \t Description: %s \t Location: %s" % (category, description, location))

    return {}
