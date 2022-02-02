from typing import List

from fastapi import HTTPException, Depends

from src.databaseSvc.databaseManipulation import EventManipulation
from src.databaseSvc.databaseSchema import Event
from ..models.events import CreateEvent


class EventService:
    def __init__(self, session=Depends(EventManipulation)):
        self.session = session

    def _get(self, event_id: str) -> dict:
        event = self.session.find_one(event_id)
        if not event:
            raise HTTPException('No event with chosen ID')
        return event

    def get_event(self, event_id: str) -> dict:
        return self._get(event_id)

    def get_list(self) -> List[dict]:
        return self.session.get_all_events()

    def create(self, event_data: CreateEvent) -> dict:
        event = Event.validate(event_data.dict(), id_needed=True)
        self.session.insert_event(event)
        return event

    def update(self, event_id: str, event_data: CreateEvent) -> dict:
        return self.session.update_event(event_id, Event.validate(event_data.dict()))

    def delete(self, event_id: str) -> Event:
        return self.session.delete_event(event_id)
