# model definition for events operations

from pydantic import BaseModel
from typing import List

class Events(BaseModel):
    id: int
    title: str
    image: str
    description: str 
    tags: list[str]
    location: str




    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https//linktomyimage.com/image.png",
                "description": "we will be discussing the contents of the FastAPI book in this event.",
                "tags": ["python", "fastapi", "book"],
                "location": "Google Meet"      
            }
        }