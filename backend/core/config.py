from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class RunConfig(BaseModel):
    port: int = 8000
    host: str = "localhost"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()


settings = Settings()
