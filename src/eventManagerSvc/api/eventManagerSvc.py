import asyncio
from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..service.eventManagerSvc import eventManagerSvc
from ..models.eventManager import AddPlayerToEvent, PlayerInfo, FullEventInfo


router = APIRouter(prefix='/event-manager')

@router.get('/get-full-event-data/{event_id}', response_model=FullEventInfo)
def get_full_event_data(event_id, manager_svc: eventManagerSvc = Depends()):
    output_info = manager_svc.get_full_event_data(event_id)
    print(output_info)
    return output_info

@router.post('/add-player/{event_id}', response_model = PlayerInfo)
def add_player_to_event(event_id: str, player_data: AddPlayerToEvent, manager_svc: eventManagerSvc = Depends()):
    added_player_data = manager_svc.add_player_to_event(event_id, player_data)
    print(added_player_data)
    return added_player_data
