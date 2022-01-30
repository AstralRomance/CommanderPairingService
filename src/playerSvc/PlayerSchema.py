class Player:

    def __init__(self, name, commander, deck_link, points, sub_points):
        self.player_name = name
        self.commander = commander
        self.deck_link = deck_link
        self.points = points
        self.sub_points = sub_points
        self.has_autowin = 0

    @staticmethod
    def encode(player):
        return {'Player_name': player.player_name,
                'Commander': player.commander,
                'Points': player.points,
                'Sub_points': player.sub_points,
                'Has_autowin': player.has_autowin}

    @staticmethod
    def decode(player):
        return Player(player['Player_name'],
                      player['Commander'],
                      player['Points'],
                      player['Sub_points'],
                      player['Has_autowin'])
