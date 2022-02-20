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
        return self.session.find_one({'Event_id': event_id})

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

    def update_player_on_event(self, event_id: str, player_id: str, player_data: dict):
        return self.session.find_one_and_update({'Event_id': event_id},
                                                {'$set': {'Players.$[element]': player_data}},
                                                array_filters=[{'element': {'$eq': {'Player_id': player_id}}}],
                                                return_document=ReturnDocument.AFTER)

    def replace_event(self, event_id: str, new_event: dict) -> dict:
        return self.session.find_one_and_replace({'Event_id': event_id}, new_event,
                                                 return_document=ReturnDocument.AFTER)

    def replace_event_as_object(self, event_id: str, new_event: Event) -> Event:
        return Event.to_object(self.replace_event(event_id, Event.to_dict(new_event)))

    def remove_player_from_event(self, event_id: str, player_id: str):
        event = self.find_event(event_id)
        if event['Status'] == 'created':
            target_document = self.session.update({'Event_id': event_id},
                                                  {'$pull': {'Players': {'Player_id': player_id}}})
        elif event['Status'] == 'started':
            target_document = self.session.find_one_and_update({'Event_id': event_id},
                                                               {'$set': {'Players.$[element]': {'Status': True}}},
                                                               array_filters = [{'element': {'$eq': {'Player_id': player_id}}}],
                                                               return_document=ReturnDocument.AFTER)
        elif event['Status'] == 'finished':
            target_document = {'error': 'Event already finished'}
        return target_document

    def update_player(self, event_id: str, player_id: str, player_data: dict):
        self.session.find_one_and_update({'Event_id': event_id},
                                         {'$set': {'Players.$[element]': player_data}},
                                         array_filters=[{'element': {'$eq': {'Player_id': player_id}}}],
                                         return_document=ReturnDocument.AFTER)

    def get_player_from_event(self, event_id: str, player_id: str):
        event = self.find_event(event_id)
        target_player = None
        for player in event['Players']:
            if player['Player_id'] == player_id:
                target_player = player
                break
        return target_player

    def get_all_event_players(self, event_id: str) -> List[dict]:
        event = self.find_event(event_id)
        event_players = event.get('Players')
        return event_players

    def add_player_into_event(self, event_id: str, player: Player) -> Event:
        return self.add_players_into_event(event_id, [player])

    def add_players_into_event(self, event_id: str, players: List[Player]) -> Event:
        event = self.find_event_as_object(event_id)
        if event.players is None:
            event.players = players
        else:
            event.players.extend(players)
        return self.replace_event_as_object(event_id, event)
