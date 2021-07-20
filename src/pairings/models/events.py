from datetime import date
from pydantic import BaseModel


class EventBase(BaseModel):
    name: str
    date: date
    players: str

    class Config:
        orm_mode = True

class Event(EventBase):
    id: int
    
    class Config:
        orm_mode = True

class EventCreate(EventBase):
    pass

    class Config:
        orm_mode = True

class EventUpdate(EventBase):
    pass

    class Config:
        orm_mode = True