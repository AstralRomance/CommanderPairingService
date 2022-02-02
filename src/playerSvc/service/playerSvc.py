from typing import List

from fastapi import Depends

from src.databaseSvc.databaseSchema import Player
from src.databaseSvc.databaseManipulation import PlayerManipulation


class PlayerService:
    def __init__(self, session = Depends(PlayerManipulation)):
        self.session = session

    def all_event_players(self, event_id: str) -> List[Player]:
        players = self.session.get_all_event_players(event_id)
        return players

    def player_on_event(self, event_id: str, player_id: int) -> Player:
        return self.session.get_player_from_event(event_id, player_id)
