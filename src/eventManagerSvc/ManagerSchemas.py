class EventManipulator:
    def __init__(self):
        pass

class Round:

    def __init__(self, number, players_per_table):
        self.number = number
        self.players_per_table = players_per_table

    @staticmethod
    def encode(event_round):
        return {'Number': event_round.number,
                'Players_per_table': [PlayersPerTable.encode(players_per_table)
                                      for players_per_table
                                      in event_round.players_per_table]}

    @staticmethod
    def decode(event_round):
        return Round(event_round['Number'],
                     [PlayersPerTable.decode(event_round)
                      for event_round
                      in event_round['Players_per_table']])


class PlayersPerTable:

    def __init__(self, table_number, players_on_table):
        self.table_number = table_number
        self.players_on_table = players_on_table

    @staticmethod
    def encode(player_per_tables):
        return {'Table_number': player_per_tables.table_number,
                'Players_on_table': [player for player in player_per_tables.players_on_table]}

    @staticmethod
    def decode(player_per_tables):
        return PlayersPerTable(player_per_tables['Table_number'],
                     [player for player in player_per_tables['Players_on_table']])
