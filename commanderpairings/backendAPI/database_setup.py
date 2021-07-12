import os
import sqlite3

def create_database():
    if 'commander_info.db' not in os.listdir():
        connection = sqlite3.connect('commander_info.db')
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE events (event_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                               event_name TEXT,
                                               event_date TEXT)''')
        cursor.execute('''CREATE TABLE players (player_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                player_name TEXT,
                                                player_commander TEXT,
                                                player_points INTEGER,
                                                player_tiebreaks INTEGER,
                                                player_event INTEGER,
                                                FOREIGN KEY(player_event) REFERENCES events(event_id)
                                                )''')
        connection.commit()
        connection.close()
    else:
        print('Database already exists')

create_database()