# model definition for user operations

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Events

class User(BaseModel):
    email: EmailStr 
    password: str
    events: Optional[List[Events]]



    class Config:
        schema_extra = {
            "example": {
                "email": fastapi@packet.com,
                "username": "strong![]",
                "events": [],

            }
        }
    


class UserSignIn(BaseModel):
    email: EmailStr
    password: str


    class Config:
        schame_extra = {
            "example": {
                "email": fastapi@packe.com,
                "password": "strong![]",
                "event": [],
            }
        }