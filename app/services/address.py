import os
import logging
import requests

from dotenv import load_dotenv

from app.schema.location import Location
from app.utils.constants import (
    RADIUS_ENDPOINT, NEAREST_RESULTS, DATASETS, SRS, RADIUS)

load_dotenv()

OS_API_KEY = os.environ.get("OS_API_KEY")

logger = logging.getLogger(__name__)


def get_nearest(location: Location):
    logger.info(f"Getting nearest location for {location}")
    # radius?maxresults=1&key=&radius=100&srs=WGS84&lr=EN&dataset=LPI,DPA&point=51.557858,0.06810
    params = {
        'key': OS_API_KEY,
        'maxresults': NEAREST_RESULTS,
        'srs': SRS,
        'point': f'{location["lat"]},{location["lng"]}',
        'radius': RADIUS,
        'dataset': DATASETS
    }

    response = requests.get(RADIUS_ENDPOINT, params=params)
    response_json = response.json()
    try:
        return response_json
    except Exception as e:
        logger.error(e)
        return {}
