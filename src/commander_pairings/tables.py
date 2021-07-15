from sqlalchemy import Column, Integer, Date, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    event_date = Column(Date)
    event_name = Column(String)
    players = Column(String)

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    player_name = Column(String)
    player_commander = Column(String)
    player_points = Column(Integer)
    player_tiebreaks = Column(Integer)
