from pydantic import BaseModel


class PlayersOnEvent(BaseModel):
    name: str
    commander: str
    points: int
    sub_points: int
    has_autowin: bool
    event_id: str


class PlayerOnEvent(PlayersOnEvent):
    player_id: int
