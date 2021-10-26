from typing import List

from pydantic import BaseModel

from .playersPerTable import PlayersPerTableBase


class RoundBase(BaseModel):
    number: int
    players_per_table: List[PlayersPerTableBase]

    class Config:
        orm_mode = True


class Event(RoundBase):
    id: int

    class Config:
        orm_mode = True


class EventCreate(RoundBase):
    pass

    class Config:
        orm_mode = True


class EventUpdate(RoundBase):
    pass

    class Config:
        orm_mode = True
