from typing import List

from pydantic import BaseModel


class DeckBase(BaseModel):
    Deck_id: str
    Deck_name: str
    Commanders: str
    Deck_link: str

    class Config:
        orm_mode = True
