from datetime import date
from typing import Optional, List

from pydantic import BaseModel, Field


class EventBase(BaseModel):
    event_name: str
    event_date: date = None
    players: str = None

class Event(BaseModel):
    id: int

    class Config:
        orm_mode = True

class EventCreate(EventBase):
    pass
