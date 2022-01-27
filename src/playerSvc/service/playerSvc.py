from fastapi import Depends

from .. import tables
from ..models.players import AddPlayerToEvent, Player


class PlayerService:
    def __init__(self, session):
        self.session = session

    def _get(self, event_id: int, player_id: int) -> tables.Player:
        return self.session.get_player_from_event(event_id, player_id)

    def add_to_event(self, event_id: int, player_info: AddPlayerToEvent) -> tables.Player:
        return self.session.add_player_on_event(event_id, player_info)

    def remove_from_event(self, event_id: int, player_id: int):
        return self.session.remove_player_from_event(event_id, player_id)

    def update_player_info(self, event_id: int, player_id: int, player_info: Player):
        return self.session.update_player_on_event(event_id, player_id, player_info)

    def get_players(self, event_id):
        return self.session.get_all_event_players(event_id)
