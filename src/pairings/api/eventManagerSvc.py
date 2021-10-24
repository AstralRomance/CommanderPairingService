from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..services.registerSvc import EventsService
from ..models.event_manager import PlayersOnEvent


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
    event_data = reg_svc._get(event_id)
    players_data = reg_svc.get_players(event_id)
    output_info = {}
    output_info['id'] = event_data.id
    output_info['name'] = event_data.name
    output_info['date'] = event_data.date
    output_info['players'] = []
    for player in players_data:
        output_info['players'].append({'player_id': player.id, 'name': player.name, 'commander': player.commander})
    return output_info
