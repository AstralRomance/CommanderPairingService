import sqlalchemy
from sqlalchemy import sql
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.Date)
    players = sqlalchemy.Column(sqlalchemy.String)

class Player(Base):
    __tablename__ = 'players'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)

