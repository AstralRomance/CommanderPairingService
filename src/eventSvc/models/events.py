from typing import List, Optional

from uuid import uuid4
from pydantic import BaseModel, validator, Field


class Player(BaseModel):
    Player_id: str                       # uuid
    Player_name: Optional[str]
    Status: bool
    Has_autowin: int
    Points: int
    Sub_points: int
    Hidden_points: float
    Commander: Optional[str]
    Deck_link: Optional[str]             # uuid

    @validator("Points", pre=True, always=True)
    def set_points(self, points):
        return points or 0

    @validator("Sub_points", pre=True, always=True)
    def set_sub_points(self, sub_points):
        return sub_points or 0

    @validator("Has_autowin", pre=True, always=True)
    def set_autowin(self, autowin):
        return autowin or False

    @validator("Status", pre=True, always=True)
    def set_status(self, status):
        return status or False

    @validator("Hidden_points", pre=True, always=True)
    def set_hidden_points(self, hidden_points):
        return hidden_points or 0

class Round(BaseModel):
    Number: int
    # Players_on_table: str А вот хз

class FullEvent(BaseModel):
    Event_id: str = Field(default_factory=uuid4)    # uuid
    Event_name: Optional[str]
    Event_Date: Optional[int]                       # unix time
    Status: Optional[str]
    Players: Optional[List[Player]]
    Rounds: Optional[List[Round]]

    @validator("Status", pre=True, always=True)
    def set_status(self, status):
        return status or False
