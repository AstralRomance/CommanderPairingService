import pymongo
from .settings import settings

class DeckOperations:
    def __init__(self):
        self.session = pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)['CommanderPairingService']['deck_database']
    
    def store_deck(self, deck_id, deck_name, commanders, deck_link):
        self.session.update({'Deck_id': deck_id, 'Deck_name': deck_name, 'Commanders': commanders, 'Deck_link': deck_link})