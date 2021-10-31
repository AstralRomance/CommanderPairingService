from typing import List

from fastapi import HTTPException

from .. import tables
from ..models.events import EventCreate, EventUpdate


class EventsService:
    def __init__(self, session):
        self.session = session

    def _get(self, event_id: int) -> tables.Event:
        event = self.session.find_one(event_id)
        if not event:
            raise HTTPException('No event with chosen ID')
        return event

    def get_list(self) -> List[tables.Event]:
        return self.session.get_events()

    def create(self, event_data: EventCreate) -> tables.Event:
        event = tables.Event.decode(**event_data.dict())
        self.session.insert_event(event)
        return event

    def update(self, event_id: int, event_data: EventUpdate) -> tables.Event:
        event = self._get(event_id)
        for field, value in event_data:
            setattr(event, field, value)
        return self.session.replace_event(event_id, event)

    def delete(self, event_id: int) -> tables.Event:
        event = self.session.delete_event(event_id)
        return event

    def get_players(self, event_id: int) -> List[tables.Player]:
        return self._get(event_id).players
