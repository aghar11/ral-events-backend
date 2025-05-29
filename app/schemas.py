# app/schemas.py

from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    name: str
    location: str
    startDate: datetime
    endDate: datetime
    url: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True
