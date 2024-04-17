from fastapi import APIRouter
from app.schema.ai import PromptInvoke
from app.services.ai import rate_issue

ai_router = APIRouter(prefix="/ai", tags=["AI"])


@ai_router.post("/invoke")
def invoke(prompt_input: PromptInvoke):
    return rate_issue(prompt_input.variables['description'])
