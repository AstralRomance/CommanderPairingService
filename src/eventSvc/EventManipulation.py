from typing import List, Dict

import pymongo
from pymongo import ReturnDocument

from .settings import settings
from .EventSchema import Event


class EventManipulation:

    def __init__(self):
        self.session = \
            pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)['CommanderPairingService']['events']

    def find_one(self, event_id: str):
        return Event.decode(self.session.find_one({'Event_id': event_id}))

    def insert_event(self, event: Event):
        self.session.insert_one(Event.encode(event))

    def get_events(self):
        return [Event.decode(event) for event in self.session.find({})]

    def delete_event(self, event_id: int):
        return Event.decode(self.session.find_one_and_delete({'Event_id': event_id}))

    def replace_event(self, event_id: int, new_event, return_document=ReturnDocument.AFTER):
        return Event.decode(self.session.find_one_and_replace({'Event_id': event_id}, Event.encode(new_event),
                            return_document=return_document))
