import datetime
import sqlite3


class PlayerProcessing:
    def create_player(self, player_name, player_commander='-'):
        connection = sqlite3.connect('commander_info.db')
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO players VALUES (?, ?, ?, ?, ?, ?)
        ''', (None, player_name, player_commander, 0, 0, None))
        connection.commit()
        cursor.close()

    def get_all_players(self):
        connection = sqlite3.connect('commander_info.db')
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM players''')
        all_players = cursor.fetchall()
        cursor.close()
        return all_players


class EventProcessing:
    def create_event(self, event_name):
        connection = sqlite3.connect('commander_info.db')
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO events VALUES (?, ?, ?)
        ''', (None, event_name, str(datetime.datetime.now())))
        connection.commit()
        cursor.close()

    def get_event_info(self, event_name):
        connection = sqlite3.connect('commander_info.db')
        cursor = connection.cursor()
        connection.row_factory = sqlite3.Row
        cursor.execute('''SELECT * FROM events WHERE event_name=?''', (event_name, ))
        event = cursor.fetchall()
        cursor.close()
        return event