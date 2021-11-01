import random


class eventManagerSvc:
    
    def __init__(self, session):
        self.session = session

    def generate_first_round(self, event_id: int):
        players = None
        shuffled_players = random.shuffle(players)
        play_tables = [shuffled_players[i:i+4] for i in range(0, len(shuffled_players), 4)]
        return play_tables

    def generate_round(self, event_id: int):
        pass
