from fastapi import Depends

from pairings.models.events import Event

from .registerSvc import EventsService
from .. import tables
from ..models.players import AddPlayerToEvent, Player


class PlayerService:
    def __init__(self, session):
        self.session = session
        self.event_service = EventsService()

    def _get(self, event_id: int, player_id: int) -> tables.Player:
        event_data = self.event_service._get(event_id)
        player_data = event_data.players(player_id)
        return player_data

    def add_to_event(self, event_id: int, player_info: AddPlayerToEvent) -> tables.Player:
        target_event = self.event_service._get(event_id)
        
        return player_data

    def remove_from_event(self, event_id: int, player_id: int):
        player_on_event = self._get(event_id, player_id)
        self.session.delete(player_on_event)
        self.session.commit()

    def update_player_info(self, event_id: int, player_id: int, player_info: Player):
        player_data = self._get(event_id, player_id)
        for field, value in player_info:
            setattr(player_data, field, value)
        self.session.commit()
        return player_data
