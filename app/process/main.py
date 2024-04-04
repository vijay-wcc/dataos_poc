from os import getenv
from dotenv import load_dotenv
from pyzeebe import create_camunda_cloud_channel, ZeebeWorker, ZeebeClient

from app.process.tasks import simple_tasks_router

load_dotenv()
CLIENT_ID = getenv("ZEEBE_CLIENT_ID")
CLIENT_SECRET = getenv("ZEEBE_CLIENT_SECRET")
CLUSTER_ID = getenv("CAMUNDA_CLUSTER_ID")
CLUSTER_REGION = getenv("CAMUNDA_CLUSTER_REGION")

channel = create_camunda_cloud_channel(CLIENT_ID, CLIENT_SECRET, CLUSTER_ID, CLUSTER_REGION)
client = ZeebeClient(channel)
worker = ZeebeWorker(channel)
worker.include_router(simple_tasks_router)
