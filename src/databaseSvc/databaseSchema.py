import uuid


class Event:

    def __init__(self, name, date, players=None, rounds=None, is_finished=None, event_id=None):
        self.name = name
        self.date = date
        if event_id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = event_id
        self.players = players
        self.rounds = rounds
        self.is_finished = is_finished

    @staticmethod
    def encode(event_class):
        event = {'Event_id': event_class.id}

        if event_class.name is not None:
            event['Event_name'] = event_class.name
        if event_class.date is not None:
            event['Event_Date'] = event_class.date
        if event_class.players is not None:
            event['Players'] = [Player.encode(player) for player in event_class.players]
        if event_class.rounds is not None:
            event['Rounds'] = [Round.encode(event_round) for event_round in event_class.rounds]
        if event_class.is_finished is not None:
            event['Is_finished'] = event_class.is_finished

        return event

    @staticmethod
    def decode(event_document):
        if event_document is None:
            return None

        return Event(event_id=event_document.get('Event_id'),
                     name=event_document.get('Event_name'),
                     date=event_document.get('Event_Date'),
                     players=None if event_document.get('Players') is None else [Player.decode(player) for player
                                                                                 in event_document.get('Players')],
                     rounds=None if event_document.get('Rounds') is None else [Round.decode(event_round) for event_round
                                                                               in event_document.get('Rounds')],
                     is_finished=event_document.get('Is_finished'))

    @staticmethod
    def validate(event_document):
        if event_document is None:
            return None

        event = {}
        if event_document.get('Event_id') is not None:
            event['Event_id'] = event_document.get('Event_id')
        if event_document.get('Event_name') is not None:
            event['Event_name'] = event_document.get('Event_name')
        if event_document.get('Event_Date') is not None:
            event['Event_Date'] = event_document.get('Event_Date')
        if event_document.get('Players') is not None:
            event['Players'] = [Player.encode(player) for player in event_document.get('Players')]
        if event_document.get('Rounds') is not None:
            event['Rounds'] = [Round.encode(event_round) for event_round in event_document.get('Rounds')]
        if event_document.get('Is_finished') is not None:
            event['Is_finished'] = event_document.get('Is_finished')

        return event


class Player:

    def __init__(self, name, points, sub_points, commander=None, deck_link=None, player_id=None, has_autowin=None):
        if player_id is None:
            self.player_id = str(uuid.uuid4())
        else:
            self.player_id = player_id
        self.player_name = name
        self.commander = commander
        self.deck_link = deck_link
        self.points = points
        self.sub_points = sub_points
        self.has_autowin = has_autowin

    @staticmethod
    def encode(player_class):
        player = {'Player_id': player_class.player_id}

        if player_class.player_name is not None:
            player['Player_name'] = player_class.player_name
        if player_class.commander is not None:
            player['Commander'] = player_class.commander
        if player_class.deck_link is not None:
            player['Deck_link'] = player_class.deck_link
        if player_class.points is not None:
            player['Points'] = player_class.points
        if player_class.sub_points is not None:
            player['Sub_points'] = player_class.sub_points
        if player_class.has_autowin is not None:
            player['Has_autowin'] = player_class.has_autowin

        return player

    @staticmethod
    def decode(player_document):
        return Player(player_id=player_document.get('Player_id'),
                      name=player_document.get('Player_name'),
                      commander=player_document.get('Commander'),
                      deck_link=player_document.get('Deck_link'),
                      points=player_document.get('Points'),
                      sub_points=player_document.get('Sub_points'),
                      has_autowin=player_document.get('Has_autowin'))


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
