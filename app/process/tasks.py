import logging

from pyzeebe import ZeebeTaskRouter
from glom import glom, Path

from app.schema.location import Location
from app.services.address import get_nearest
from app.services.notifications import send_text
simple_tasks_router = ZeebeTaskRouter()

logger = logging.getLogger(__name__)

first_result_path = Path('results', 0, 'LPI')


@simple_tasks_router.task(task_type="enrich_event")
async def add_postcode(location: Location):
    logger.info("Location: %s" % location)
    nearest = get_nearest(location)
    address = glom(nearest, first_result_path)
    logger.info("Nearest: %s \t ,Address: %s " % (nearest, address))
    if nearest is not None:
        return {
            "post_code": glom(address, "POSTCODE_LOCATOR"),
        }
    else:
        return {
            "post_code": ""
        }


@simple_tasks_router.task(task_type="text_officer")
async def text_inspector(template_id: str, post_code: str, officer: str):
    logger.info("Notify Officer: %s" % officer)
    nearest = send_text(template_id=template_id, personalisation={
        "post_code": post_code,
        "officer": officer
    })
    logger.info("Nearest: %s" % nearest)
    return {}
