import aiohttp
from commanderpairings.models import setup_db
from commanderpairings import create_app

app = create_app()

if __name__ == '__main__':
    setup_db.setup_db()
    aiohttp.web.run_app(app)
