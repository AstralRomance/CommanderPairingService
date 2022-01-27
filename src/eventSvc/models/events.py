from datetime import datetime
from typing import List

from pydantic import BaseModel



class Event(BaseModel):
    Event_name: str
    Event_Date: datetime
    Event_id: str

    class Config:
        orm_mode = True

class CreateEvent(BaseModel):
    Event_name: str
    Event_Date: datetime
    Event_id: str
