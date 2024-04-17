from pydantic import BaseModel, Field


class PromptInvoke(BaseModel):
    template: str = Field(
        default=None, title="Prompt", max_length=300
    )
    variables: dict = Field(
        default=None, title="Variables",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "template": """
                    Given the {description} tell RAG rate the issue 
                    format the output with the key: rag
                    the value of rag should one of Red, Amber or Green only
                    """,
                    "variables": {
                        "description": "The car alarm is unbearable and has been going off for last 15 minutes"
                    }
                }
            ]
        }
    }


class RAG(BaseModel):
    rating: str = Field(description="rag rating of the issue")
