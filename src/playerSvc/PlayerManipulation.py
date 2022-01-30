from typing import List, Dict

import pymongo
from pymongo import ReturnDocument

from .settings import settings
from .PlayerSchema import Player


class PlayerManipulation:

    def __init__(self):
        self.session = pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)['CommanderPairingService']['events']

    # This is template for utility search user in database without event_id. Future feature will require it.
    def find_one(self):
        pass

    def get_player_from_event(self, event_id: int, player_id: int) -> Player:
        event = self.session.find_one({'Event_id': event_id})
        target_player = None
        for player in event.get('Players'):
            if player['Player_id'] == player_id:
                target_player = player
                break
        return target_player

    def get_all_event_players(self, event_id: int):
        event = self.session.find_one({'Event_id': event_id})
        event_players = event.get('Players')
        return event_players
