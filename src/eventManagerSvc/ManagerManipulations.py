from typing import List, Dict

import pymongo
from pymongo import ReturnDocument

from .settings import settings
#from .ManagerSchemas import Event, Player


class ManagerManipulations:

    def __init__(self):
        self.session = pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)['CommanderPairingService']['events']

    def get_full_event_data(self):
        pass

    # def insert_event(self, event: Event):
    #     self.session.insert_one(Event.encode(event))

    # def find_event(self, event_id: int):
    #     return Event.decode(self.session.find_one({'Event_id': event_id}))

    # def find_events(self, events_id: List[int]):
    #     return [Event.decode(self.session.find_one({'Event_id': event_id})) for event_id in events_id]

    # def get_events(self):
    #     return [Event.decode(event) for event in self.session.find({})]

    # def delete_event(self, event_id: int):
    #     return Event.decode(self.session.find_one_and_delete({'Event_id': event_id}))

    # def replace_event(self, event_id: int, new_event, return_document=ReturnDocument.AFTER):
    #     return Event.decode(self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(new_event)))

    # def get_player_from_event(self, event_id: int, player_id: int):
    #     event = Event.decode(self.session.find_one({'Event_id': event_id}))
    #     target_player = None
    #     for player in event.players:
    #         if player['Player_id'] == player_id:
    #             target_player = player
    #             break
    #     return target_player

    # def add_player_on_event(self, event_id: int, player_data, return_document=ReturnDocument.AFTER):
    #     event = Event.decode(self.session.find_one({'Event_id': event_id}))
    #     event.players.append(player_data)
    #     self.session.find_one_and_replace({'Event_id': event_id})
    #     return event

    # def remove_player_from_event(self, event_id: int, player_id: int, return_document=ReturnDocument.AFTER):
    #     event = Event.decode(self.session.find_one({'Event_id': event_id}))
    #     for player in event.players:
    #         if player['Player_id'] == player_id:
    #             event.players.remove(player)
    #             break
    #     self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event))
    #     return event

    # def update_player_on_event(self, event_id: int, player_id: int, player_data):
    #     event = Event.decode(self.session.find_one({'Event_id': event_id}))
    #     for player in event.players:
    #         if player['Player_id'] == player_id:
    #             for field in player_data.keys():
    #                 player[field] = player_data[field]
    #             break
    #     self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event))
    #     return event

    # def change_player_points(self, event_id: int, player_id: int, player_points: Dict):
    #     event = Event.decode(self.session.find_one({'Event_id': event_id}))
    #     for player in event.players:
    #         if player['Player_id'] == player_id:
    #             player['Points'] += player_points['points']
    #             player['Sub_points'] += player_points['sub_points']
    #     self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event))

    # def get_all_event_players(self, event_id: int) -> List[Player]:
    #     event = Event.decode(self.session.find_one({'Event_id': event_id}))
    #     return event.players

    # def add_round_to_event(self, event_id: int, round_data: List[Dict]):
    #     event = Event.decode(self.session.find_one({'Event_id': event_id}))
    #     event['Rounds'].append(round_data)
    #     self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(event))
    #     return event
