import logging
from pyzeebe import ZeebeTaskRouter

from app.schema.location import Location
from app.services.ai import rate_issue as rate_issue_ai

noise_tasks_router = ZeebeTaskRouter()

logger = logging.getLogger(__name__)


@noise_tasks_router.task(task_type="receive_event")
async def receive_event(category: str, description: str, location: Location):
    logger.info("Received Event")
    logger.info("Category: %s \t Description: %s \t Location: %s" % (category, description, location))


@noise_tasks_router.task(task_type="rate_issue")
async def rate_issue(description: str):
    logger.info("Description: %s" % description)
    rating = rate_issue_ai(description)
    rag = rating.get('status', 'Green').upper()
    logger.info("RAG: %s " % rag)
    return {
        'rag': rag
    }


@noise_tasks_router.task(task_type="salesforce_submit")
async def salesforce_submit(rag: str):
    logger.info("Salesforce Submission")
    logger.info("RAG: %s" % rag)
    return {}


@noise_tasks_router.task(task_type="submit_case")
async def submit_case(category: str, description: str, location: Location):
    logger.info("Case Submission")
    logger.info("Category: %s \t Description: %s \t Location: %s" % (category, description, location))
    return {}


"""

{
    "category": "Car Alarm",
    "description": "The car alarm is unbearable and has been going off for last 15 minutes",
    "location": {
        "lat": 51.4975531,
        "lng": -0.1373525
    }
}

{
    "category": "House",
    "description": "Loud music coming from neighbours house",
    "location": {
        "lat": 51.4975531,
        "lng": -0.1373525
    }
}
"""
