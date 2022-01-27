from typing import List
from pydantic import BaseModel
from .events import Event
from .players import PlayerToReturn


class FullEventData(Event):
    players: List[PlayerToReturn]

class PlayersPerTable(BaseModel):
    pass
