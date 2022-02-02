from typing import List

from pydantic import BaseModel


class EventBase(BaseModel):
    Event_name: str
    Event_Date: str
    Event_id: str

    class Config:
        orm_mode = True


class CreateEvent(BaseModel):
    Event_name: str
    Event_Date: str
