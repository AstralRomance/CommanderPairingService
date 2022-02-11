from uuid import uuid4
from fastapi import Depends
from databaseSvc.analyticOperations import DeckOperations

class deckSvc: 
    def __init__(self, session = Depends(DeckOperations)):
        self.session = session
    
    def add_deck(self, deck_name, commanders, deck_link):
        self.session.store_deck(str(uuid4()), deck_name, commanders, deck_link)