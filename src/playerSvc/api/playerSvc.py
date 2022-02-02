from fastapi import APIRouter, Depends
from ..service.playerSvc import PlayerService

router = APIRouter(prefix='/players')

@router.get('/player_on_event/{event_id}/{player_id}')
def get_event_player(event_id: str, player_id: int, service: PlayerService = Depends()):
    return service.player_on_event(event_id, player_id)

@router.get('/players_on_event/{event_id}')
def get_all_event_players(event_id: str, service: PlayerService = Depends()):
    return service.all_event_players(event_id)
