from os import getenv
from dotenv import load_dotenv
from pyzeebe import ZeebeWorker, ZeebeClient, create_insecure_channel  # create_camunda_cloud_channel

from app.process.tasks import simple_tasks_router
from app.process.noise import noise_tasks_router

load_dotenv()
CLIENT_ID = getenv("ZEEBE_CLIENT_ID")
CLIENT_SECRET = getenv("ZEEBE_CLIENT_SECRET")
CLUSTER_ID = getenv("CAMUNDA_CLUSTER_ID")
CLUSTER_REGION = getenv("CAMUNDA_CLUSTER_REGION")

# channel = create_camunda_cloud_channel(CLIENT_ID, CLIENT_SECRET, CLUSTER_ID, CLUSTER_REGION)
channel = create_insecure_channel()
client = ZeebeClient(channel)
worker = ZeebeWorker(channel)
worker.include_router(simple_tasks_router)
worker.include_router(noise_tasks_router)
