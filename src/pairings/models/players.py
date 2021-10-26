from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    commander: str
    points: int
    sub_points: int

class AddPlayerToEvent(PlayerBase):
    event_id: int

    class Config:
        orm_mode = True

class RemovePlayerFromEvent(BaseModel):
    event_id: int
    player_id: int

    class Config:
        orm_mode = True

class PlayerToReturn(PlayerBase):
    player_id: int
