from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 8000
    database_url: str
    player_svc_host = '0.0.0.0'
    player_svc_port = 8001
    event_svc_host = '0.0.0.0'
    event_svc_port = 8002


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)
