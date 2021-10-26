from typing import List
from datetime import datetime
from pydantic import BaseModel

from .players import PlayerBase
from .round import RoundBase

# Зачем base?
class EventBase(BaseModel):
    name: str
    date: datetime
    id: int
    players: List[PlayerBase]
    rounds: List[RoundBase]

    class Config:
        orm_mode = True

class Event(EventBase):
    
    class Config:
        orm_mode = True

class EventCreate(EventBase):
    pass

    class Config:
        orm_mode = True

class EventUpdate(EventBase):
    pass

    class Config:
        orm_mode = True
