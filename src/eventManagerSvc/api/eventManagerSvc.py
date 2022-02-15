import asyncio
from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..service.eventManagerSvc import eventManagerSvc
from ..models.eventManager import AddPlayerToEvent, PlayerInfo, GeneralEventInfo, UpdatePlayerPoints, FullEventInfo


router = APIRouter(prefix='/event-manager')

@router.get('/get-full-event-data/{event_id}', response_model=GeneralEventInfo)
def get_full_event_data(event_id, manager_svc: eventManagerSvc = Depends()):
    output_info = manager_svc.get_full_event_data(event_id)
    print(output_info)
    return output_info

@router.post('/add-player/{event_id}', response_model = PlayerInfo)
def add_player_to_event(event_id: str, player_data: AddPlayerToEvent, manager_svc: eventManagerSvc = Depends()):
    added_player_data = manager_svc.add_player_to_event(event_id, player_data)
    return added_player_data

@router.delete('/remove-player/{event_id}/{player_id}', response_model = GeneralEventInfo)
def remove_player_from_event(event_id: str, player_id: str, manager_svc: eventManagerSvc = Depends()):
    updated_event_data = manager_svc.remove_player_from_event(event_id, player_id)
    return updated_event_data

@router.put('/update-player-points/{event_id}/{player_id}', response_model = PlayerInfo)
def update_player_points(event_id: str, player_id: str, player_data: UpdatePlayerPoints, manager_svc: eventManagerSvc = Depends()):
    actual_player_data = manager_svc.update_player_info(event_id, player_id, player_data)
    return actual_player_data

#, response_model = FullEventInfo
@router.put('/generate-round/{event_id}')
def generate_round(event_id: str, round_number: int, manager_svc: eventManagerSvc = Depends()):
    manager_svc.generate_round(event_id, round_number)
    output_info = manager_svc.get_full_event_data(event_id)
    print('**********************')
    print(output_info)
    return output_info
