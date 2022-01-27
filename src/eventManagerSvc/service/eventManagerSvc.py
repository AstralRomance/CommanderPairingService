import random
from typing import Dict

from .playerSvc import PlayerService



class eventManagerSvc:
    
    def __init__(self, session):
        self.session = session

    def generate_first_round(self, event_id: int):
        players = PlayerService.get_players(event_id)
        shuffled_players = random.shuffle(players)
        play_tables = [shuffled_players[i:i+4] for i in range(0, len(shuffled_players), 4)]
        if len(play_tables[-1]) < 3:
            for player in play_tables[-1]:
                self._change_autowins(player)
                self.change_players_point(event_id, player["Player_id"], {'points': 2, 'Sub_points': 1})
        self._add_round(event_id, 1, play_tables)
        return play_tables

    def generate_round(self, event_id: int):
        pass

    def change_players_point(self, event_id: int, player_id: int, points: Dict):
        self.session.change_player_points(event_id, player_id, points)
    
    def _add_round(self, event_id: int, round_num: int, tables_data):
        self.session.add_round_to_event(event_id, round_num, tables_data)
    
    def _change_autowins(self, player, duration: int = 3):
        player['Has_autowin'] = duration

