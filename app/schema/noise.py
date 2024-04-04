from enum import Enum

from pydantic import BaseModel, Field

from app.schema.location import Location


class NoiseCategory(str, Enum):
    construction = "Construction"
    car_alarm = "Car Alarm"
    other = "Other"


class NoiseSubmit(BaseModel):
    category: NoiseCategory = Field(
        default=None, title="Category of Noise", max_length=300
    )
    description: str = Field(
        default=None, title="Description of Noise", max_length=300
    )
    location: Location = Field(
        default=None, title="Location of Noise",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "category": "Construction",
                    "description": "Very loud construction noises",
                    "location": {
                        "lat": 51.4975531,
                        "lng": -0.1373525
                    }
                }
            ]
        }
    }
