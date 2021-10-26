from typing import List

from pydantic import BaseModel


class PlayersPerTableBase(BaseModel):
    table_number: int
    players_on_table: List[str]

    class Config:
        orm_mode = True


class PlayersPerTable(PlayersPerTableBase):
    id: int

    class Config:
        orm_mode = True


class EventCreate(PlayersPerTableBase):
    pass

    class Config:
        orm_mode = True


class EventUpdate(PlayersPerTableBase):
    pass

    class Config:
        orm_mode = True
