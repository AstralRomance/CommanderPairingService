import sqlite3


class Player:
    def add_player(self, event_token: str, player_name: str, commander: str) -> None:
        conn = sqlite3.connect('events_database.db')
        add_player_request = 'INSERT INTO players(event_jwt, player_name, player_commander, player_points, player_ties) VALUES(?,?,?,?,?)'
        add_player_cursor = conn.cursor()
        add_player_cursor.execute(add_player_request, (event_token, player_name, commander, 0, 0))
        conn.commit()

    def add_player_points(self, points: int, ties: int) -> None:
        pass
