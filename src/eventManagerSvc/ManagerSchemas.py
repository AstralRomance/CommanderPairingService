class EventManipulator:
    def __init__(self, event_name, event_date, event_id,
                 players):
        self.event_name = event_name
        self.event_date = event_date
        self.event_id = event_id
        self.players = players

    #This implementation is temporary for test refactoring
    @staticmethod
    def encode(event):
        return {'event':{
                         'Event_name': event.Event_name,
                         'Event_Date': event.Event_Date,
                         'Event_id': event.Event_id
                        },
                'players':event.Players
        }

    @staticmethod
    def decode(event):
        return EventManipulator(event['event'],
                                event['players'])
