from typing import List

from pydantic import BaseModel


class PlayersPerTable(BaseModel):
    table_number: int
    players_on_table: List[str]

    class Config:
        orm_mode = True


class EventCreate(PlayersPerTable):
    pass

    class Config:
        orm_mode = True


class EventUpdate(PlayersPerTable):
    pass

    class Config:
        orm_mode = True
