from fastapi import APIRouter, Depends

from ..models.players import (
    Player,
    AddPlayerToEvent,
    PlayerToReturn
)
from ..service.playerSvc import PlayerService

router = APIRouter(
    prefix='/players'
)


@router.post('/add-to-event', response_model=PlayerToReturn)
def add_player(player_data: AddPlayerToEvent, service: PlayerService = Depends()):
    service.add_to_event(player_data)
    return player_data


@router.put('/update-on-event/{event_id}/{player_id}', response_model=PlayerToReturn)
def update_player(event_id: int, player_id: int, player_data: Player, service: PlayerService = Depends()):
    service.update_player_info(event_id, player_id, player_data)
    return player_data


@router.delete('/remove-from-event/{event_id}/{player_id}', response_model=PlayerToReturn)
def remove_player(event_id: int, player_id: int, service: PlayerService = Depends()):
    service.remove_from_event(event_id, player_id)
