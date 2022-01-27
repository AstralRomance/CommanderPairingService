from pydantic import BaseModel


class Player(BaseModel):
    name: str
    commander: str
    points: int
    sub_points: int


class AddPlayerToEvent(Player):
    event_id: int

    class Config:
        orm_mode = True


class RemovePlayerFromEvent(BaseModel):
    event_id: int
    player_id: int

    class Config:
        orm_mode = True


class PlayerToReturn(Player):
    player_id: int
