from datetime import datetime
from typing import List

from pydantic import BaseModel

from .players import Player
from .round import Round


class Event(BaseModel):
    name: str
    date: datetime
    id: int
    players: List[Player]
    rounds: List[Round]

    class Config:
        orm_mode = True


class EventCreate(Event):
    pass

    class Config:
        orm_mode = True


class EventUpdate(Event):
    pass

    class Config:
        orm_mode = True
