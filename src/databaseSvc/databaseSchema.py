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
    def to_dict(event_object):
        event = {'Event_id': event_object.id}

        if event_object.name is not None:
            event['Event_name'] = event_object.name
        if event_object.date is not None:
            event['Event_Date'] = event_object.date
        if event_object.players is not None:
            event['Players'] = [Player.to_dict(player) for player in event_object.players]
        if event_object.rounds is not None:
            event['Rounds'] = [Round.to_dict(event_round) for event_round in event_object.rounds]
        if event_object.is_finished is not None:
            event['Is_finished'] = event_object.is_finished

        return event

    @staticmethod
    def to_object(event_dict):
        if event_dict is None:
            return None

        return Event(event_id=event_dict.get('Event_id'),
                     name=event_dict.get('Event_name'),
                     date=event_dict.get('Event_Date'),
                     players=None if event_dict.get('Players') is None else [Player.to_object(player) for player
                                                                             in event_dict.get('Players')],
                     rounds=None if event_dict.get('Rounds') is None else [Round.to_object(event_round) for event_round
                                                                           in event_dict.get('Rounds')],
                     is_finished=event_dict.get('Is_finished'))

    @staticmethod
    def validate(event_dict, id_needed=False):
        if event_dict is None:
            return None

        event = {}
        if event_dict.get('Event_id') is not None:
            event['Event_id'] = event_dict.get('Event_id')
        elif id_needed:
            event['Event_id'] = str(uuid.uuid4())
        if event_dict.get('Event_name') is not None:
            event['Event_name'] = event_dict.get('Event_name')
        if event_dict.get('Event_Date') is not None:
            event['Event_Date'] = event_dict.get('Event_Date')
        if event_dict.get('Players') is not None:
            event['Players'] = [Player.to_dict(player) for player in event_dict.get('Players')]
        if event_dict.get('Rounds') is not None:
            event['Rounds'] = [Round.to_dict(event_round) for event_round in event_dict.get('Rounds')]
        if event_dict.get('Is_finished') is not None:
            event['Is_finished'] = event_dict.get('Is_finished')

        return event


class Player:

    def __init__(self, name, points, sub_points, commander=None, deck_link=None, player_id=None, has_autowin=None,
                 status=None):
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
        self.status = status

    @staticmethod
    def to_dict(player_object):
        player = {'Player_id': player_object.player_id}

        if player_object.player_name is not None:
            player['Player_name'] = player_object.player_name
        if player_object.commander is not None:
            player['Commander'] = player_object.commander
        if player_object.deck_link is not None:
            player['Deck_link'] = player_object.deck_link
        if player_object.points is not None:
            player['Points'] = player_object.points
        if player_object.sub_points is not None:
            player['Sub_points'] = player_object.sub_points
        if player_object.has_autowin is not None:
            player['Has_autowin'] = player_object.has_autowin
        if player_object.status is not None:
            player['Status'] = player_object.status

        return player

    @staticmethod
    def to_object(player_dict):
        return Player(player_id=player_dict.get('Player_id'),
                      name=player_dict.get('Player_name'),
                      commander=player_dict.get('Commander'),
                      deck_link=player_dict.get('Deck_link'),
                      points=player_dict.get('Points'),
                      sub_points=player_dict.get('Sub_points'),
                      has_autowin=player_dict.get('Has_autowin'),
                      status=player_dict.get('Status'))


class Round:

    def __init__(self, number, players_per_table=None):
        self.number = number
        self.players_per_table = players_per_table

    @staticmethod
    def to_dict(round_object):
        round_dict = {'Number': round_object.number}

        if round_object.players_per_table is not None:
            round_dict['Players_per_table'] = [PlayersPerTable.to_dict(players_per_table)
                                               for players_per_table
                                               in round_object.players_per_table]

        return round_dict

    @staticmethod
    def to_object(round_dict):
        return Round(round_dict.get('Number'),
                     players_per_table=None if round_dict.get('Players_per_table') is None else [
                         PlayersPerTable.to_object(event_round)
                         for event_round
                         in round_dict['Players_per_table']])


class PlayersPerTable:

    def __init__(self, table_number, players_on_table=None):
        self.table_number = table_number
        self.players_on_table = players_on_table

    @staticmethod
    def to_dict(player_per_tables_object):
        player_per_tables = {'Table_number': player_per_tables_object.table_number}
        if player_per_tables_object.players_on_table is not None:
            player_per_tables['Players_on_table'] = [player_id for player_id in
                                                     player_per_tables_object.players_on_table]

        return player_per_tables

    @staticmethod
    def to_object(player_per_tables_dict):
        return PlayersPerTable(player_per_tables_dict['Table_number'],
                               players_on_table=None if player_per_tables_dict.get('Players_on_table') is None else
                               [player_id for player_id in player_per_tables_dict['Players_on_table']])
