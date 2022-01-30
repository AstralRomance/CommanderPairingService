from datetime import datetime
from typing import List

from pydantic import BaseModel



class EventBase(BaseModel):
    Event_name: str
    Event_Date: datetime
    Event_id: int

    class Config:
        orm_mode = True

class CreateEvent(BaseModel):
    Event_name: str
    Event_Date: datetime
