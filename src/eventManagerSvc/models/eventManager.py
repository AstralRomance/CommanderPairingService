from typing import List, Union
from datetime import datetime
from pydantic import BaseModel
    

class AddPlayerToEvent(BaseModel):
    Player_name: str
    Commander: str
    Deck_link: Union[str, None]

class PlayerInfo(AddPlayerToEvent):
    Player_id: str
    Player_name: str
    Commander: str
    Deck_link: Union[str, None]
    Points: int
    Sub_points: int

class BaseEvenForPlayer(BaseModel):
    Event_id: str
    player_data: AddPlayerToEvent

class PlayerBase(BaseModel):
    Player_id: int
    Player_name: str
    Commander: str
    Deck_link: str
    Points: int
    Sub_points: int
    Has_autowin: bool

class UpdatePlayerPoints(BaseModel):
    Points: int
    Sub_points: int

class GeneralEventInfo(BaseModel):
    Event_id: str
    Event_name: str
    Event_Date: datetime
    Players: List[PlayerInfo]

class FullEventInfo(BaseModel):
    pass
