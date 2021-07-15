from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.event import EventCreate

class EventsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all_events(self) -> List[tables.Event]:
        events = (
            self.session
            .query(tables.Event)
            .all()
        )
        return events

    def create_event(self, event_data: EventCreate) -> tables.Event:
        event = tables.Event(**event_data.dict())
        self.session.add(event)
        self.session.commit()
        return event