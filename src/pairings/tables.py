class Event:

    def __init__(self, name, date, event_id, players, rounds, is_finished=True):
        self.name = name
        self.date = date
        self.id = event_id
        self.players = players
        self.rounds = rounds
        self.is_finished = is_finished

    @staticmethod
    def encode(event_class):
        return {'Event_name': event_class.name,
                'Event_Date': event_class.date,
                'Event_id': event_class.id,
                'Players': [Player.encode(player) for player in event_class.players],
                'Rounds': [Round.encode(event_round) for event_round in event_class.rounds],
                'Is_finished': event_class.is_finished}

    @staticmethod
    def decode(event_document):
        return Event(event_document['Event_name'],
                     event_document['Event_Date'],
                     event_document['Event_id'],
                     [Player.decode(player) for player in event_document['Players']],
                     [Round.decode(event_round) for event_round in event_document['Rounds']],
                     event_document['Is_finished'])


class Player:

    def __init__(self, player_id, name, commander, deck_link, points, sub_points, has_autowin=0):
        self.player_id = player_id
        self.player_name = name
        self.commander = commander
        self.deck_link = deck_link
        self.points = points
        self.sub_points = sub_points
        self.has_autowin = has_autowin

    @staticmethod
    def encode(player_class):
        return {'Player_id': player_class.player_id,
                'Player_name': player_class.player_name,
                'Commander': player_class.commander,
                'Deck_link': player_class.deck_link,
                'Points': player_class.points,
                'Sub_points': player_class.sub_points,
                'Has_autowin': player_class.has_autowin}

    @staticmethod
    def decode(player_document):
        return Player(player_document['Player_id'],
                      player_document['Player_name'],
                      player_document['Commander'],
                      player_document['Deck_link'],
                      player_document['Points'],
                      player_document['Sub_points'],
                      player_document['Has_autowin'])


class Round:

    def __init__(self, number, players_per_table):
        self.number = number
        self.players_per_table = players_per_table

    @staticmethod
    def encode(round_class):
        return {'Number': round_class.number,
                'Players_per_table': [PlayersPerTable.encode(players_per_table)
                                      for players_per_table
                                      in round_class.players_per_table]}

    @staticmethod
    def decode(round_document):
        return Round(round_document['Number'],
                     [PlayersPerTable.decode(event_round)
                      for event_round
                      in round_document['Players_per_table']])


class PlayersPerTable:

    def __init__(self, table_number, players_on_table):
        self.table_number = table_number
        self.players_on_table = players_on_table

    @staticmethod
    def encode(player_per_tables_class):
        return {'Table_number': player_per_tables_class.table_number,
                'Players_on_table': [player for player in player_per_tables_class.players_on_table]}

    @staticmethod
    def decode(player_per_tables_document):
        return PlayersPerTable(player_per_tables_document['Table_number'],
                               [player for player in player_per_tables_document['Players_on_table']])
