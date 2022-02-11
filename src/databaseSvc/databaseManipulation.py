from typing import List, Dict

import pymongo
from pymongo import ReturnDocument

from .settings import settings
from .databaseSchema import Event, Player


class DataBaseManipulation:

    def __init__(self):
        self.session = \
            pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)['CommanderPairingService'][
                'events']

    def find_event(self, event_id: str) -> dict:
        return self.session.find_event({'Event_id': event_id})

    def find_event_as_object(self, event_id: str) -> Event:
        return Event.to_object(self.find_event(event_id))

    def insert_event(self, event: dict):
        self.session.insert_one(event)

    def insert_event_as_object(self, event: Event):
        self.insert_event(Event.to_dict(event))

    def get_all_events(self) -> List[dict]:
        return [event for event in self.session.find({})]

    def get_all_events_as_objects(self) -> List[Event]:
        return [Event.to_object(event) for event in self.get_all_events()]

    def delete_event(self, event_id: str):
        return self.session.find_one_and_delete({'Event_id': event_id})

    def update_event(self, event_id: str, new_values: dict) -> dict:
        return self.session.find_one_and_update({'Event_id': event_id}, {'$set': new_values},
                                                return_document=ReturnDocument.AFTER)

    def replace_event(self, event_id: str, new_event: dict) -> dict:
        return self.session.find_one_and_replace({'Event_id': event_id}, new_event,
                                                 return_document=ReturnDocument.AFTER)

    def replace_event_as_object(self, event_id: str, new_event: Event) -> Event:
        return Event.to_object(self.replace_event(event_id, Event.to_dict(new_event)))

    def remove_player_from_event(self, event_id: str, player_id: str) -> Event:
        event = self.find_event_as_object(event_id)
        if event.players is None:
            return event
            # Todo: Возвращать ошибку?
        event.players = [player for player in event.players if player.player_id != player_id]
        return self.replace_event_as_object(event_id, event)

    def update_player_info(self, event_id: str, player_id: str, player_data: dict) -> Player:
        target_event = self.find_event(event_id)
        target_player = None
        if target_event.get('Players') is None:
            return None
            # Todo: Возвращать ошибку?
        for player in target_event['Players']:
            if player['Player_id'] == player_id:
                target_player = player
                for key, value in player_data.items():
                    player[key] = value
                    # Todo: += или = ?
        self.replace_event(event_id, target_event)
        return Player.to_object(target_player)

    def get_player_from_event(self, event_id: str, player_id: str) -> Player:
        event = self.find_event(event_id)
        target_player = None
        if event.get('Players') is None:
            return None
            # Todo: Возвращать ошибку?
        for player in event['Players']:
            if player['Player_id'] == player_id:
                return Player.to_object(target_player)
        return None
        # Todo: Возвращать ошибку?

    def get_all_event_players(self, event_id: str) -> List[dict]:
        event = self.find_event(event_id)
        event_players = event.get('Players')
        return event_players
        # Todo: Вернётся None если никого не было

    def add_player_into_event(self, event_id: str, player: Player) -> Event:
        return self.add_players_into_event(event_id, [player])

    def add_players_into_event(self, event_id: str, players: List[Player]) -> Event:
        event = self.find_event_as_object(event_id)
        if event.players is None:
            event.players = players
        else:
            event.players.extend(players)
        return self.replace_event_as_object(event_id, event)
