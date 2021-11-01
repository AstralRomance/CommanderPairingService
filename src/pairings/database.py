from typing import List

import pymongo
from pymongo import ReturnDocument

from .settings import settings
from .tables import Event, Player


class Database:

    def __init__(self):
        self.session = \
            pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)["CommanderPairingService"][
                "events"]

    def insert_event(self, event: Event):
        self.session.insert_one(Event.encode(event))

    def find_event(self, event_id: int):
        return Event.decode(self.session.find_one({"Event_id": event_id}))

    def find_events(self, events_id: List[int]):
        return [Event.decode(self.session.find_one({"Event_id": event_id})) for event_id in events_id]

    def get_events(self):
        return [Event.decode(event) for event in self.session.find({})]

    def delete_event(self, event_id: int):
        return Event.decode(self.session.find_one_and_delete({"Event_id": event_id}))

    def replace_event(self, event_id: int, new_event, return_document=ReturnDocument.AFTER):
        return Event.decode(self.session.find_one_and_replace({"Event_id": event_id}, Event.encode(new_event)))

    def insert_player_to_event(self, event_id: int, player_data, return_document=ReturnDocument.AFTER):
        event = Event.decode(self.session.find_one_and_update({"Event_id": event_id}))
        event.players.append(player_data)
        return event

    def remove_player_from_event(self, event_id: int, player_id: int, return_document=ReturnDocument.AFTER):
        event = Event.decode(self.session.find_one({"Event_id": event_id}))
        for player in event.players:
            if player["Player_id"] == player_id:
                event.players.remove(player)
                break
        self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event))
        return event

    def update_player_on_event(self, event_id: int, player_id: int, player_data):
        event = Event.decode(self.session.find_one({"Event_id": event_id}))
        for player in event.players:
            if player['Player_id'] == player_id:
                for field in player_data.keys():
                    player[field] = player_data[field]
                break
        self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event))
        return event
