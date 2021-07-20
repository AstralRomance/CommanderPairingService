from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.events import EventCreate, EventUpdate


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
