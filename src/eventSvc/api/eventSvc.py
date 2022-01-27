from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..models.events import Event, CreateEvent
from ..service.eventSvc import EventService


router = APIRouter(
    prefix='/events'
)

@router.get('/', response_model=List[Event])
def get_events(service: EventService=Depends()):
    return service.get_list()

@router.post('/', response_model = Event)
def create_event(event_data: CreateEvent, service: EventService = Depends()):
    return service.create(event_data)

@router.put('/{event_id}', response_model = Event)
def update_event(event_id: int, event_data: Event, service: EventService = Depends()):
    return service.update(event_id, event_data)

@router.delete('/{event_id}')
def delete_event(event_id: int, service: EventService = Depends()):
    service.delete(event_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
