import asyncio
import json
import random
import aiohttp
import jwt
import datetime
from dateutil import parser
from aiohttp_jinja2 import template

@template('index.html')
async def index(request):
    return {}

@template('pairings.html')
async def pairings(request):
    return {}

def get_players(request):
    session_headers = request.headers
    current_file = jwt.decode(session_headers['authorization'], 'secret', algorithms=['HS256'])['current_file']
    event_players = {}
    with open(f'Events/{current_file}', 'r') as event_file:
        event_players = json.load(event_file)
    return aiohttp.web.json_response(event_players)

def gen_token(filename: str, datetime_now: datetime.datetime) -> str:
    encoded_jwt = jwt.encode({'current_file': filename,'date_end':str(datetime_now+datetime.timedelta(days=1))}, 'secret', algorithm='HS256')
    return encoded_jwt

async def get_token(request):
    datetime_now = datetime.datetime.now()
    current_filename = f'Event_{str(datetime_now)}.json'
    with open(f'Events/{current_filename}', 'w') as event_file:
        json.dump({'event date': str(datetime_now), 'players':[]}, event_file)
    token = gen_token(current_filename, datetime_now)
    return aiohttp.web.json_response({'jwt':token})

async def validate_token(request):
    session_headers = request.headers
    current_token_finish = jwt.decode(session_headers['authorization'], 'secret', algorithms=['HS256'])['date_end']
    is_valid = (datetime.datetime.now() < parser.parse(current_token_finish))
    return aiohttp.web.json_response({'is_valid': is_valid})

async def add_player(request):
    player_info = await request.json()
    session_headers = request.headers
    current_filename = jwt.decode(session_headers['authorization'], 'secret', algorithms=['HS256'])['current_file']
    event_info = {}
    with open(f'Events/{current_filename}', 'r') as event_file:
        event_info = json.load(event_file)
        event_info['players'].append({'player_name':player_info[0], 'player_commander':player_info[1], 'points':0})
    with open(f'Events/{current_filename}', 'w') as event_file:
        json.dump(event_info, event_file)
    return aiohttp.web.json_response(event_info)

async def make_pairings(request):
    event_info = await request.json()
    session_headers = request.headers
    current_filename = jwt.decode(session_headers['authorization'], 'secret', algorithms=['HS256'])['current_file']
    event_dict = {}
    players_list = []
    with open(f'Events/{current_filename}', 'r') as event_file:
        event_dict = json.load(event_file)
        players_list = event_dict['players']
    points_set = set([point for point in players_list['points']])
    players_per_point = {}
    for point_val in points_set:
        temp = []
        for player in players_list:
            if int(player['points']) == point_val:
                temp.append(player['player_name'])
        players_per_point[point_val] = temp.copy()
        
