from typing import List
from pydantic import BaseModel
from .events import Event
from .players import PlayerToReturn


class PlayersOnEvent(Event):
    players: List[PlayerToReturn]
