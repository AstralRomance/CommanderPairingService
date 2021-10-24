from fastapi import Depends
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.players import AddPlayerToEvent, PlayerBase


class PlayerService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, event_id: int, player_id: int) -> tables.Player:
        player_data = self.session.query(tables.Player).filter_by(event_id = event_id).filter_by(event_id = event_id).first()
        return player_data

    def add_to_event(self, player_info: AddPlayerToEvent) -> tables.Player:
        player_data = tables.Player(**player_info.dict())
        self.session.add(player_data)
        self.session.commit()
        return player_data

    def remove_from_event(self, event_id: int, player_id: int):
        player_on_event = self._get(event_id, player_id)
        self.session.delete(player_on_event)
        self.session.commit()

    def update_player_info(self, event_id: int, player_id: int, player_info: PlayerBase):
        player_data = self._get(event_id, player_id)
        for field, value in player_info:
            setattr(player_data, field, value)
        self.session.commit()
        return player_data
