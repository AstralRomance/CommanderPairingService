from curses import raw
from typing import List
from ast import operator
from uuid import uuid4
import random
from loguru import logger
from copy import copy
from operator import itemgetter

from fastapi import Depends

from databaseSvc.databaseManipulation import DataBaseManipulation
from databaseSvc.databaseSchema import Player, Event


class eventManagerSvc:
    def __init__(self, session=Depends(DataBaseManipulation)):
        self.session = session

    def gen_default_player_params(self, player_data: dict) -> dict:
        player_data['Points'] = 0
        player_data['Sub_points'] = 0
        player_data['Has_autowin'] = 0
        player_data['Hidden_points'] = 0
        player_data['Status'] = False
        return player_data

    def gen_player_hidden_points(self, turn_postition: int, round_number: int, points: int, sub_points: int) -> float:
        '''
            This is only my fantasies, we need to discuss this thing. This is only template for calculating points.
        '''
        position_coefficient = 1 + (turn_postition / 10)
        round_coefficient = 1 + round_number / 10 if round_number > 1 else 1
        return (points * position_coefficient * round_coefficient) + sub_points / 15

    def get_full_event_data(self, event_id: str) -> Event:
        return Event.to_dict(self.session.find_event_as_object(event_id))

    def change_event_state(self, event_id: str, target_state: str):
        return self.session.change_event_status(event_id, {'Status': target_state})

    def update_player_on_event(self, event_id: str, player_id: str, player_data: dict):
        return self.session.update_player_on_event(event_id, player_id, player_data)

    def add_player_to_event(self, event_id: str, player_data: dict) -> Player:
        target_event = self.session.find_event_as_object(event_id)
        target_player_data = self.gen_default_player_params(copy(dict(player_data)))
        target_player_data = Player.to_object(target_player_data)
        if target_event.players:
            target_event.players.append(target_player_data)
        else:
            target_event.players = [target_player_data]
        self.session.replace_event_as_object(event_id, target_event)
        return Player.to_dict(target_player_data)

    def remove_player_from_event(self, event_id: str, player_id: str) -> Event:
        remove_player_response = self.session.remove_player_from_event(event_id, player_id)
        response = None
        if remove_player_response.get('error'):
            response = 'Event finished' # Change this to http exception
        if not remove_player_response:
            response = None # Change to 404 response
        response = remove_player_response
        return response

    def update_player_points(self, event_id: str, player_id: str, round_number: int, player_data: dict):
        target_event = self.session.find_event(event_id)
        target_player = self.session.get_player_from_event(event_id, player_id)
        target_round = None
        for event_round in target_event.get('Rounds'):
            if event_round['Number'] == round_number:
                target_round = event_round
                break
        if target_round:
            tables = target_round['Players_on_table']
            player_turn_position = None
            for table in tables:
                table_players = tables[table]
                player_turn_position = table_players.index(player_id) if player_id in table_players else None
                if player_turn_position:
                    break
            if not player_turn_position:
                return None
            player_hidden_points = self.gen_player_hidden_points(player_turn_position, round_number,
                                                                 int(target_player['Points']), int(target_player['Sub_points']))
            target_player['Points'] += player_data.Points
            target_player['Sub_points'] += player_data.Sub_points
            if target_player.get('Hidden_points'):
                target_player['Hidden_points'] += player_hidden_points
            else:
                target_player['Hidden_points'] = player_hidden_points
            self.session.update_player(event_id, player_id, target_player)
        else:
            target_player = None # Replace to not found reponse
        return target_player

    def generate_round(self, event_id: str, round_number: int):
        '''
            THIS THING ALREADY NEEDS REFACTORING.
        '''
        target_event = self.session.find_event(event_id)
        event_players = [player for player in target_event['Players']]
        event_players_map = {player['Player_id']: player['Hidden_points'] for player in event_players}
        event_players_map = {k: v for k, v in sorted(event_players_map.items(), key=itemgetter(1), reverse=True)}
        if round_number == 1:
            for _ in range(5):
                random.shuffle(list(event_players_map.items()))
            event_players_map = dict(event_players_map)
        else:
            event_players_map = {k: v for k, v in sorted(event_players_map.items(), key=itemgetter(1), reverse=True)}
        players_on_tables = [list(event_players_map.keys())[i:i + 4] for i in range(0, len(event_players_map), 4)]

        # Give buys to players
        if len(players_on_tables[-1]) < 3:
            for player in players_on_tables[-1]:
                for raw_player in event_players:
                    if player == raw_player['Player_id']:
                        raw_player['Has_autowin'] = 3
                        self.session.update_player(event_id, player, raw_player)
                        break
            players_on_tables.pop()
        print(players_on_tables)
        [random.shuffle(table) for table in players_on_tables]
        print(players_on_tables)
        target_event['Rounds'].append({'Number': round_number, 'Players_on_table': {str(table_num+1): players_on_tables[table_num] for table_num in range(len(players_on_tables))}})
        actual_event_data = self.session.update_event(event_id, target_event)
        return actual_event_data
