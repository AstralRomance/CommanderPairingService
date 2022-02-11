from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..service.eventManagerSvc import eventManagerSvc
from ..models.eventManager import FullEventInfo, PlayerInfo


router = APIRouter(prefix='/event-manager')

@router.get('/get-full-event-data/{event_id}', response_model=FullEventInfo)
async def get_full_event_data(event_id, manager_svc: eventManagerSvc = Depends()):
    output_info = await manager_svc.get_full_event_data(event_id)
    return output_info

@router.post('change-players-points/{event_id}/{player_id}', response_model=PlayerInfo)
def change_player_points(event_id: str, player_id: int, manager_svc: eventManagerSvc = Depends()):
    player_data = manager_svc.change_player_points(event_id, player_id)
    return player_data
