from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.events import EventCreate, EventUpdate
from ..models.players import AddPlayerToEvent, RemovePlayerFromEvent


class EventsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, event_id: int) -> tables.Event:
        events = (
            self.session
            .query(tables.Event)
            .filter_by(id=event_id)
            .first()
        )
        if not events:
            raise HTTPException('No event with chosen ID')
        return events

    def get_list(self) -> List[tables.Event]:
        events = (
            self.session
            .query(tables.Event)
            .all()
        )
        return events

    def create(self, event_data: EventCreate) -> tables.Event:
        event = tables.Event(**event_data.dict())
        self.session.add(event)
        self.session.commit()
        return event

    def update(self, event_id: int, event_data: EventUpdate) -> tables.Event:
        event = self._get(event_id)
        for field, value in event_data:
            setattr(event, field, value)
        self.session.commit()
        return event

    def delete(self, event_id: int):
        event = self._get(event_id)
        self.session.delete(event)
        self.session.commit()

    def get_players(self, event_id: int) -> List[tables.Player]:
        players = self.session.query(tables.Player).filter_by(event_id = event_id).all()
        return players

class PlayerService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def add_to_event(self, player_info: AddPlayerToEvent) -> tables.Player:
        player_data = tables.Player(**player_info.dict())
        self.session.add(player_data)
        self.session.commit()
        return player_data

    def remove_from_event(self, event_id: int, player_id: int):
        player_on_event = self.session.query(tables.Player).filter_by(id = player_id).filter_by(event_id = event_id).limit(10).offset(0).first()
        self.session.delete(player_on_event)
        self.session.commit()
