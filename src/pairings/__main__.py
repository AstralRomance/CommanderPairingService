import json

import uvicorn

from .database import get_session
from .settings import settings
from .tables import Event

session = get_session()["CommanderPairingService"]["events"]

event = Event.decode(json.loads("""{
        "Event_name": "string",
        "Event_Date": "Date",
        "Event_id": "integer",
        "Players": [
            {
                "Player_name": "string",
                "Commander": "string",
                "Points": "integer",
                "Sub_points": "integer"
            }
        ],
        "Rounds": [
            {
                "Number": "integer",
                "Players_per_table": [
                    {
                        "Table_number": "integer",
                        "Players_on_table": ["Player", "Player", "Player", "Player"]
                    }
                ]
            }
        ]
    }"""))

session.insert_one(Event.encode(event))

uvicorn.run(
    'pairings.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
