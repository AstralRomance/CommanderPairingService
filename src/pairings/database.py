import pymongo

from .settings import settings
from .tables import Event


class Database:

    def __init__(self):
        self.session = \
            pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)["CommanderPairingService"][
                "events"]

    def insert_event(self, event):
        self.session.insert_one(Event.encode(event))

    def find_event(self, event_id):
        return Event.decode(self.session.find_one({"Event_id": event_id}))

    def find_events(self, events_id):
        return [Event.decode(self.session.find_one({"Event_id": event_id})) for event_id in events_id]

    def get_events(self):
        return [Event.decode(event) for event in self.session.find({})]

    def delete_event(self, event_id):
        return Event.decode(self.session.find_one_and_delete({"Event_id": event_id}))
