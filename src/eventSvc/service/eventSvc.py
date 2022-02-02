from typing import List

from fastapi import HTTPException, Depends

from ..models.events import EventBase, CreateEvent
from src.databaseSvc.databaseSchema import Event
from src.databaseSvc.databaseManipulation import EventManipulation


class EventService:
    def __init__(self, session=Depends(EventManipulation)):
        self.session = session

    def _get(self, event_id: str) -> Event:
        event = self.session.find_one(event_id)
        if not event:
            raise HTTPException('No event with chosen ID')
        return event

    def get_event(self, event_id: str) -> List[EventBase]:
        event = self._get(event_id)
        return Event.encode(event)

    def get_list(self) -> List[Event]:
        return [Event.encode(event) for event in self.session.get_events()]

    def create(self, event_data: CreateEvent) -> Event:
        event = Event.decode(event_data.dict())
        self.session.insert_event(event)
        return Event.encode(event)

    def update(self, event_id: str, event_data: Event) -> Event:
        event = self._get(event_id)
        event.date = str(event_data.Event_Date)
        event.name = event_data.Event_name
        return Event.encode(self.session.replace_event(event_id, event))

    def delete(self, event_id: str) -> Event:
        event = self.session.delete_event(event_id)
        return event
