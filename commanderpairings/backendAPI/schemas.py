from typing import Optional

from pydantic import BaseModel, Field

class Player(BaseModel):
    player_name: str = Field(...)
    player_commander: Optional[str] = None
    player_points: int = 0
    player_tiebreaks: int = 0

    class Config:
        orm_mode = True

class Event(BaseModel):
    event_name: str = Field(...)
    event_date: str = None
    event_players: list = None

    class Config:
        orm_mode = True
