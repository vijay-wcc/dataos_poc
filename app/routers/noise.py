from fastapi import APIRouter

from app.process.main import client
from app.schema.noise import NoiseSubmit

noise_router = APIRouter(prefix="/noise", tags=["Noise"])


@noise_router.post("/submit")
async def submit(noise_data: NoiseSubmit):
    process_instance_key = await client.run_process("Noise_PoC", noise_data.dict())
    return {"process_instance_key": process_instance_key}
