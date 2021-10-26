from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..services.registerSvc import EventsService
from ..models.event_manager import PlayersOnEvent
from ..tables import Event

router = APIRouter(prefix='/event-manager')


@router.put('/create-new-round/{event_id}/{round_number}')
def create_new_round(event_id: int, round_number: int):
    pass

@router.put('/change-player-points/{event_id}')
def change_player_points(event_id: int, players_info: List[str]):
    pass

@router.post('/finish-event/{event_id}')
def finish_event(event_id: int):
    pass

@router.get('/get-full-event-data/{event_id}', response_model=PlayersOnEvent)
def get_full_event_data(event_id, reg_svc: EventsService = Depends()):

    output_info = Event.decode(event_data)

    return output_info
