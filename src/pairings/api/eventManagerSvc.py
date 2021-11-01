from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..services.registerSvc import EventsService
from ..services.eventManagerSvc import eventManagerSvc
from ..models.event_manager import FullEventData, PlayersOnEvent, PlayersPerTable
from ..tables import Event

router = APIRouter(prefix='/event-manager')


@router.put('/create-new-round/{event_id}/{round_number}', response_model=PlayersPerTable)
def create_new_round(event_id: int, round_number: int, service: eventManagerSvc = Depends()):
    if round_number == 1:
        playing_tables = service.generate_first_round(event_id)
        service.add_round(playing_tables)
    else:
        service.generate_round(event_id)

@router.put('/change-player-points/{event_id}')
def change_player_points(event_id: int, players_info: List[str]):
    pass

@router.post('/finish-event/{event_id}')
def finish_event(event_id: int):
    pass

@router.get('/get-full-event-data/{event_id}', response_model=FullEventData)
def get_full_event_data(event_id, reg_svc: EventsService = Depends()):
    output_info = reg_svc.get_full_event_data(event_id)
    return output_info
