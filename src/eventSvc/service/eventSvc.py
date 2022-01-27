from typing import List

from fastapi import HTTPException, Depends

from ..models.events import Event, CreateEvent
from .. import tables
from ..database import EventManipulation


class EventService:
    def __init__(self, session = Depends(EventManipulation)):
        self.session = session

    def _get(self, event_id: str) -> tables.Event:
        event = self.session.find_one(event_id)
        if not event:
            raise HTTPException('No event with chosen ID')
        return event

    def get_list(self) -> List[Event]:
        return [tables.Event.encode(event) for event in self.session.get_events()]

    def create(self, event_data: CreateEvent) -> Event:
        event = tables.Event.decode(event_data.dict())
        self.session.insert_event(event)
        return tables.Event.encode(event)

    def update(self, event_id: str, event_data: Event) -> tables.Event:
        event = self._get(event_id)
        for field, value in event_data:
            setattr(event, field, value)
        return self.session.replace_event(event_id, event)

    def delete(self, event_id: str) -> tables.Event:
        event = self.session.delete_event(event_id)
        return event
