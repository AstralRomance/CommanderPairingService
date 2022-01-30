from typing import Dict
import random
import asyncio

from fastapi import Depends
from httpx import AsyncClient

from ..ManagerManipulations import ManagerManipulations


class eventManagerSvc:
    def __init__(self, session = Depends(ManagerManipulations)):
        self.session = session

    async def request(self, client: AsyncClient, url: str, request_params: dict = None):
        response = await client.get(url, params=request_params)
        return response.json()

    async def task(self, target_url: str, request_params: dict = None):
        async with AsyncClient() as client:
            result = await self.request(client, target_url, request_params)
        return result

    async def get_full_event_data(self, event_id):
        event_url = f'http://0.0.0.0:8002/events/{event_id}'
        players_url = f'http://0.0.0.0:8001/players/players_on_event/{event_id}'
        event_data = await self.task(event_url)
        players_data = await self.task(players_url)
        output = {'event': event_data, 'players': players_data}
        return output
