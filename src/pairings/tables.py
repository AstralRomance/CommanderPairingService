import sqlalchemy
from sqlalchemy import sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.Date)
    players = sqlalchemy.Column(sqlalchemy.String)

    child_table = relationship('Player', uselist=True, back_populates='parent_table')

class Player(Base):
    __tablename__ = 'players'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    event_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('events.id'))
    name = sqlalchemy.Column(sqlalchemy.String)
    commander = sqlalchemy.Column(sqlalchemy.String)

    parent_table = relationship('Event', uselist=True, back_populates='child_table')
