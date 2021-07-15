import json
import datetime
from fastapi import FastAPI

from .api import router

app = FastAPI()
app.include_router(router)


# @app.post('/create-event/')
# async def create_event(event: Event):
#     my_event_info = event.dict()
#     event_processing = EventProcessing()
#     event_processing.create_event(my_event_info['event_name'])
#     return event_processing.get_event_info(my_event_info['event_name'])


# @app.post('/create-player/')
# async def create_player(player: Player):
#     player_info = player.dict()
#     create_player = PlayerProcessing()
#     create_player.create_player(player_info['player_name'], player_info['player_commander'])
#     return create_player.get_all_players()
    


# @app.get('/')
# async def root():
#     return {'message': 'Hello world'}
