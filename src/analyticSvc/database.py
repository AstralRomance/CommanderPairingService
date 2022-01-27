from typing import List, Dict

import pymongo
from pymongo import ReturnDocument

from .settings import settings
from .tables import Event, Player


class Database:

    def __init__(self):
        self.session = pymongo.MongoClient(settings.database_url)['CommanderPairingService']['events']

    def insert_event(self, event: Event):
        self.session.insert_one(Event.encode(event))

    def find_event(self, event_id: str) -> Event:
        return Event.decode(self.session.find_one({'Event_id': event_id}))

    def find_events(self, events_id: List[str]) -> List[Event]:
        return [Event.decode(self.session.find_one({'Event_id': event_id})) for event_id in events_id]

    def get_events(self) -> List[Event]:
        return [Event.decode(event) for event in self.session.find({})]

    def delete_event(self, event_id: str) -> Event:
        return Event.decode(self.session.find_one_and_delete({'Event_id': event_id}))

    def replace_event(self, event_id: str, new_event) -> Event:
        return Event.decode(self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(new_event),
                                                              return_document=ReturnDocument.AFTER))

    def get_player_from_event(self, event_id: str, player_id: int) -> Player:
        event = Event.decode(self.session.find_one({'Event_id': event_id}))
        target_player = None
        for player in event.players:
            if player.player_id == player_id:
                target_player = player
                break
        return target_player

    def add_player_on_event(self, event_id: str, player_data) -> Event:
        event = Event.decode(self.session.find_one({'Event_id': event_id}))
        event.players.append(player_data)
        return Event.decode(self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event),
                                                              return_document=ReturnDocument.AFTER))

    def remove_player_from_event(self, event_id: str, player_id: int) -> Event:
        event = Event.decode(self.session.find_one({'Event_id': event_id}))
        for player in event.players:
            if player.player_id == player_id:
                event.players.remove(player)
                break
        return Event.decode(self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event),
                                                              return_document=ReturnDocument.AFTER))

    def update_player_on_event(self, event_id: str, player_id: int, player_data) -> Event:
        event = Event.decode(self.session.find_one({'Event_id': event_id}))
        for player in event.players:
            if player.player_id == player_id:
                for field in player_data.keys():
                    player[field] = player_data[field]
                break
        return Event.decode(self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event),
                                                              return_document=ReturnDocument.AFTER))

    def change_player_points(self, event_id: str, player_id: int, player_points: Dict) -> Event:
        event = Event.decode(self.session.find_one({'Event_id': event_id}))
        for player in event.players:
            if player.player_id == player_id:
                player.points += player_points['points']
                player.sub_points += player_points['sub_points']
        return Event.decode(
            self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event),
                                              return_document=ReturnDocument.AFTER))

    def get_all_event_players(self, event_id: str) -> List[Player]:
        event = Event.decode(self.session.find_one({'Event_id': event_id}))
        return event.players

    def add_round_to_event(self, event_id: str, round_data: List[Dict]) -> Event:
        event = Event.decode(self.session.find_one({'Event_id': event_id}))
        event.rounds.append(round_data)
        return Event.decode(
            self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event),
                                              return_document=ReturnDocument.AFTER))
