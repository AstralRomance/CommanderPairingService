from uuid import uuid4


import pymongo
from .settings import settings

class DeckOperations:
    def __init__(self):
        self.session = pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)['CommanderPairingService']['deck_database']
        self.deck_database_document_name = 'cedh_decks'
    
    def store_deck(self, deck_id, deck_name, commanders, deck_link):
        self.session.update({'deck_database': self.deck_database_document_name},
        {'Deck_id': deck_id, 'Deck_name': deck_name, 'Commanders': commanders, 'Deck_link': deck_link}, upsert=True)
