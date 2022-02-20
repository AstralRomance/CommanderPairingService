from typing import Optional
from pydantic import BaseModel, validator


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
