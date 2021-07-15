from typing import List
from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from commander_pairings import services

from .. import tables
from ..models.event import Event, EventCreate
from ..services.events import EventsService

router = APIRouter(
    prefix='/events'
)

@router.get('/', response_model = List[Event])
def get_events(service: EventsService = Depends()):
    print(service.get_all_events())
    return service.get_all_events()

@router.post('/create_event')
def create_event(event_data: EventCreate, service: EventsService = Depends()):
    return service.create_event(event_data)
