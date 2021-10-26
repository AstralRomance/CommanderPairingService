import pymongo

from .settings import settings


def get_session():
    client = pymongo.MongoClient(settings.database_url, serverSelectionTimeoutMS=5000)
    try:
        print(client.server_info())
        yield client
    finally:
        client.close()
