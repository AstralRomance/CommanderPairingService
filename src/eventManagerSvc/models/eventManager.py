from typing import List
from datetime import datetime
from pydantic import BaseModel


class EventInfo(BaseModel):
    Event_name: str
    Event_Date: datetime
    Event_id: str

class PlayerInfo(BaseModel):
    Player_id: int
    Player_name: str
    Commander: str
    Deck_link: str
    Points: int
    Sub_points: int
    Has_autowin: bool

class FullEventInfo(BaseModel):
    event: EventInfo
    players: List[PlayerInfo]
