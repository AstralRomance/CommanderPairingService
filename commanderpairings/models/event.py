import sqlite3
import datetime
import jwt


class Event:
    def add_event(self, jwt_token: str, event_name: str, event_date: str) -> None:
        conn = sqlite3.connect('events_database.db')
        add_event_request = 'INSERT INTO events(event_jwt, event_name, event_date) VALUES(?,?,?)'
        add_event_cursor = conn.cursor()
        add_event_cursor.execute(add_event_request, (jwt_token, event_name, str(datetime.datetime.now())))
        conn.commit()
