from uuid import uuid4
import random
from loguru import logger
from copy import copy

from fastapi import Depends

from databaseSvc.databaseManipulation import EventManipulation
from databaseSvc.databaseSchema import Player, Event


class eventManagerSvc:
    def __init__(self, session=Depends(EventManipulation)):
        self.session = session

    def gen_default_player_params(self, player_data: dict) -> dict:
        player_data['Points'] = 0
        player_data['Sub_points'] = 0
        player_data['Has_autowin'] = 0
        return player_data

    def get_full_event_data(self, event_id: str) -> Event:
        return Event.encode(self.session.find_one_as_object(event_id))

    def add_player_to_event(self, event_id: str, player_data: dict) -> Player:
        target_event = self.session.find_one_as_object(event_id)
        target_player_data = self.gen_default_player_params(copy(dict(player_data)))
        target_player_data = Player.decode(target_player_data)
        logger.debug(target_player_data)
        if target_event.players:
            target_event.players.append(target_player_data)
        else:
            target_event.players = [target_player_data]
        self.session.replace_event_as_object(event_id, target_event)
        return Player.encode(target_player_data)
