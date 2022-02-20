from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..models.events import CreateEvent, FullEvent
from ..service.eventSvc import EventService

router = APIRouter(
    prefix='/events'
)


@router.get('/', response_model=List[FullEvent])
def get_events(service: EventService = Depends()):
    return service.get_list()


@router.get('/{event_id}', response_model=FullEvent)
def get_event(event_id: str, service: EventService = Depends()):
    return service.get_event(event_id)


@router.post('/', response_model=FullEvent)
def create_event(event_data: FullEvent, service: EventService = Depends()):
    return service.create(event_data)


@router.put('/{event_id}', response_model=FullEvent)
def update_event(event_id: str, event_data: FullEvent, service: EventService = Depends()):
    return service.update(event_id, event_data)


@router.delete('/{event_id}')
def delete_event(event_id: str, service: EventService = Depends()):
    return service.delete(event_id)
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
