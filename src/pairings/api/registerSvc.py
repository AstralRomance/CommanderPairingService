from typing import List

from fastapi import APIRouter, Depends, Response, status

from pairings import services
from pairings.models.players import RemovePlayerFromEvent

from .. import tables
from ..database import Session, get_session
from ..models.events import (
    Event,
    EventCreate,
    EventUpdate
)
from ..models.players import (
    PlayerBase,
    AddPlayerToEvent
)
from ..services.registerSvc import EventsService, PlayerService


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

@router.get('/players/get-players/{event_id}')
def get_event_players(event_id: int, service: EventsService = Depends()):
    return service.get_players(event_id)

@router.post('/players/add-player', response_model = PlayerBase)
def add_player(player_data: AddPlayerToEvent, service: PlayerService = Depends()):
    service.add_to_event(player_data)
    return player_data

@router.delete('/players/remove-player/{event_id}/{player_id}', response_model=PlayerBase)
def remove_player(event_id: int, player_id: int, service: PlayerService = Depends()):
    service.remove_from_event(event_id, player_id)
