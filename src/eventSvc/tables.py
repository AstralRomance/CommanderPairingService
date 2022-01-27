class Event:

    def __init__(self, name, date, event_id):
        self.name = name
        self.date = date
        self.id = event_id
        self.is_finished = False

    @staticmethod
    def encode(event):
        return {'Event_name': event.name,
                'Event_Date': event.date,
                'Event_id': event.id}

    @staticmethod
    def decode(event):
        return Event(event['Event_name'],
                     event['Event_Date'],
                     event['Event_id'])
