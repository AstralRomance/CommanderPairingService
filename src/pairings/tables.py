class Event:

    def __init__(self, name, date, event_id, players, rounds):
        self.name = name
        self.date = date
        self.id = event_id
        self.players = players
        self.rounds = rounds

    @staticmethod
    def encode(event):
        return {"Event_name": event.name,
                "Event_Date": event.date,
                "Event_id": event.id,
                "Players": [Player.encode(player) for player in event.players],
                "Rounds": [Round.encode(event_round) for event_round in event.rounds]}

    @staticmethod
    def decode(event):
        return Event(event["Event_name"],
                     event["Event_Date"],
                     event["Event_id"],
                     [Player.decode(player) for player in event["Players"]],
                     [Round.decode(event_round) for event_round in event["Rounds"]])


class Player:

    def __init__(self, name, commander, points, sub_points):
        self.player_name = name
        self.commander = commander
        self.points = points
        self.sub_points = sub_points

    @staticmethod
    def encode(player):
        return {"Player_name": player.player_name,
                "Commander": player.commander,
                "Points": player.points,
                "Sub_points": player.sub_points}

    @staticmethod
    def decode(player):
        return Player(player["Player_name"],
                      player["Commander"],
                      player["Points"],
                      player["Sub_points"])


class Round:

    def __init__(self, number, players_per_table):
        self.number = number
        self.players_per_table = players_per_table

    @staticmethod
    def encode(event_round):
        return {"Number": event_round.number,
                "Players_per_table": [PlayersPerTable.encode(players_per_table)
                                      for players_per_table
                                      in event_round.players_per_table]}

    @staticmethod
    def decode(event_round):
        return Round(event_round["Number"],
                     [PlayersPerTable.decode(event_round)
                      for event_round
                      in event_round["Players_per_table"]])


class PlayersPerTable:

    def __init__(self, table_number, players_on_table):
        self.table_number = table_number
        self.players_on_table = players_on_table

    @staticmethod
    def encode(player_per_tables):
        return {"Table_number": player_per_tables.table_number,
                "Players_on_table": [player for player in player_per_tables.players_on_table]}

    @staticmethod
    def decode(player_per_tables):
        return PlayersPerTable(player_per_tables["Table_number"],
                     [player for player in player_per_tables["Players_on_table"]])
