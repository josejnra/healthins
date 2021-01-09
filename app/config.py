import os

from pydantic import BaseSettings


class Settings(BaseSettings):

    base_url: str

    project_id: str
    google_credentials: str
    pubsub_topic: str

    class Config:
        case_sensitive = True
        env_file = os.environ.get('ENV_FILE_PATH')


settings = Settings()
