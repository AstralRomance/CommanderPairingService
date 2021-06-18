import os
import sqlite3


def setup_db():
    if 'players_database.db' not in os.listdir():
        sqlite3.connect('events_database.db')
        conn = sqlite3.connect('events_database.db')
        create_table_cursor = conn.cursor()
        # CREATE TABLE EVENTS
        try:
            request = 'CREATE TABLE events([event_jwt] text PRIMARY KEY, [event_name] text, [event_date] text)'
            create_table_cursor.execute(request)
        except Exception as e:
            return {'success': False, 'error': e}
        # CREATE TABLE
        try:
            request = 'CREATE TABLE players([event_jwt] text FOREIGN KEY, [player_name] text, [player_commander] text, [player_points] INTEGER, [player_ties] INTEGER)'
            create_table_cursor.execute(request)
        except Exception as e:
            return {'success': False, 'error': e}
        conn.commit()
    return {'success': True, 'error': None}
