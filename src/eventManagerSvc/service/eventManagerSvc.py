from uuid import uuid4
import random
from loguru import logger
from copy import copy

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
        return player_data

    def get_full_event_data(self, event_id: str) -> Event:
        return Event.to_dict(self.session.find_event_as_object(event_id))

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
        return Event.to_dict(self.session.remove_player_from_event(event_id, player_id))

    def update_player_info(self, event_id: str, player_id: str, player_data: dict) -> Player:
        return Player.to_dict(self.session.update_player_info(event_id, player_id, player_data))

    def generate_round(self, event_id: str, round_number: int):
        if round_number == 1:
            target_event = self.session.find_event(event_id)
            event_players = target_event['Players']
            for _ in range(5):
                random.shuffle(event_players)
            target_event_players = [event_players[i:i + 4] for i in range(0, len(event_players), 4)]
            target_event['Rounds'] = [{"Number": round_number,
                                       "Players_per_table": {str(table_num + 1): target_event_players[table_num] for
                                                             table_num in range(len(target_event_players))}}]
            self.session.update_event(event_id, target_event)
        else:
            pass
