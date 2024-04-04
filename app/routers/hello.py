from fastapi import APIRouter

hello_router = APIRouter(prefix="/simple", tags=["simple"])


@hello_router.get("/")
async def root():
    return {"message": "Hello World"}


@hello_router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
