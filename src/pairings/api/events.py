from typing import List

from fastapi import APIRouter, Depends, Response, status

from pairings import services

from .. import tables
from ..database import Session, get_session
from ..models.events import (
    Event,
    EventCreate,
    EventUpdate
)
from ..services.events import EventsService


router = APIRouter(
    prefix='/events'
)

@router.get('/', response_model=List[Event])
def get_events(service: EventsService=Depends()):
    return service.get_list()

@router.post('/', response_model = Event)
def create_event(event_data: EventCreate, service: EventsService = Depends()):
    return service.create(event_data)

@router.put('/{event_id}', response_model = Event)
def update_event(event_id: int, event_data: EventUpdate, service: EventsService = Depends()):
        return service.update(event_id, event_data)

@router.delete('/{event_id}')
def delete_event(event_id: int, service: EventsService = Depends()):
    service.delete(event_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)