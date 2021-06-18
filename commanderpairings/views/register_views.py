import asyncio
import json
import random
import aiohttp
import jwt
from dateutil import parser
from aiohttp_jinja2 import template

from .utilities.utilities import gen_token, validate_token
from .models.player import Player
from .models.event import Event


@template('index.html')
async def index(request):
    #FOR FUTURE, WHEN ADD EVENT NAME
    #event_info = await request.json()
    event_info = {'event_name': f'EDH event {random.randint(1, 1000)}', 'event_date': str(datetime.datetime.now())}
    if validate_token(request.headers['authorization']):
        return aiohttp.web.json_response({'validate': 'Old', 'token': request.headers['authorization']})
    else:
        jwt_token = jwt.encode(event_info, 'secret', algorithm='HS256')
        Event().add_event(jwt_token, event_info['event_name'], event_info['event_date'])
        return aiohttp.web.json_response({'validate': 'New', 'token': jwt_token})

async def add_player(request):
    player_info = await request.json()
    try:
        Player().add_player(request.headers['authorization'], player_info['player'], player_info['commander'])
    except Exception as e:
        print('add player view')
        print(e)
        return aiohttp.web.json_response({'success': False, 'error': str(e)})
    return aiohttp.web.json_response({'success': True, 'error': None})
