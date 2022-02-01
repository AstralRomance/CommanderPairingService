from typing import Dict
import random
import asyncio

from fastapi import Depends
from httpx import AsyncClient

from src.databaseSvc.databaseManipulation import ManagerManipulations


class eventManagerSvc:
    def __init__(self, session=Depends(ManagerManipulations)):
        # This class temporary use API requests.
        # In https://github.com/AstralRomance/CommanderPairingService/issues/6
        # will be implemented separated module to interract with data base
        self.session = session
        self.base_events_url = 'http://0.0.0.0:8002/events/'
        self.base_players_url = 'http://0.0.0.0:8001/players/'

    async def request(self, client: AsyncClient, url: str, request_params: dict = None):
        response = await client.get(url, params=request_params)
        return response.json()

    async def task(self, target_url: str, request_params: dict = None):
        async with AsyncClient() as client:
            result = await self.request(client, target_url, request_params)
        return result

    async def get_full_event_data(self, event_id):
        event_url = f'{self.base_events_url}{event_id}'
        players_url = f'{self.base_players_url}players_on_event/{event_id}'
        event_data = await self.task(event_url)
        players_data = await self.task(players_url)
        output = {'event': event_data, 'players': players_data}
        return output
