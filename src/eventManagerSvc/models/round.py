from typing import List

from pydantic import BaseModel

from .playersPerTable import PlayersPerTable


class Round(BaseModel):
    number: int
    players_per_table: List[PlayersPerTable]

    class Config:
        orm_mode = True


class Event(Round):
    id: int

    class Config:
        orm_mode = True


class Create(Round):
    pass

    class Config:
        orm_mode = True


class Update(Round):
    pass

    class Config:
        orm_mode = True
