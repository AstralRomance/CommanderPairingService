from typing import List

from fastapi import HTTPException, Depends

from databaseSvc.databaseManipulation import DataBaseManipulation
from databaseSvc.databaseSchema import Event
from ..models.events import FullEvent


class EventService:
    def __init__(self, session=Depends(DataBaseManipulation)):
        self.session = session

    def _get(self, event_id: str) -> dict:
        event = self.session.find_event(event_id)
        if not event:
            raise HTTPException(404, 'No event with chosen ID')
        return event

    def get_event(self, event_id: str) -> dict:
        return self._get(event_id)

    def get_list(self) -> List[dict]:
        return self.session.get_all_events()

    def create(self, event_data: FullEvent) -> FullEvent:
        if event_data.Status is None:
            event_data['Status'] = 'created'
        self.session.insert_event(event_data)
        return event_data

    def update(self, event_id: str, event_data: FullEvent) -> dict:
        return self.session.update_event(event_id, event_data.dict())

    def delete(self, event_id: str) -> Event:
        return self.session.delete_event(event_id)
