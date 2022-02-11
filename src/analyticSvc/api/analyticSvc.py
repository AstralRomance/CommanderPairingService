from typing import List
from fastapi import APIRouter, Depends, Response, status
from ..models.decks import DeckBase
from ..service.decks import deckSvc

router = APIRouter(
    prefix='/analytics'
)

@router.get('/decks', response_model=List[DeckBase])
def get_decks(service):
    pass

@router.post('/decks')
def add_deck(deck_name: str, commanders: str, deck_link: str, deck_svc: deckSvc = Depends()):
    output_info = deck_svc.add_deck(deck_name, commanders, deck_link)
    return output_info
