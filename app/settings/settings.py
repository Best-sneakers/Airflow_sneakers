__all__ = "settings"

import os
from functools import lru_cache

from pydantic_settings import BaseSettings


class Celery(BaseSettings):
    class Config:
        env_prefix = "CELERY_"

    max_loop_interval: str = "60"


class Redis(BaseSettings):
    class Config:
        env_prefix = "REDIS_"

    host: str = "localhost"
    port: int = 6379
    db: int = 1


class RabbitMQ(BaseSettings):
    class Config:
        env_prefix = "RABBITMQ_"

    host: str = "localhost"
    port: int = 5672
    username: str = "parser"
    password: str = "parser"


class DB(BaseSettings):
    class Config:
        env_prefix = "POSTGRES_"

    db: str = "parser"
    user: str = "postgres"
    password: str = "password"
    host: str = "localhost"
    port: int = 5432


class UvicornURL(BaseSettings):
    """Represents Uvicorn settings"""

    class Config:
        env_prefix = "UVICORN_"

    host: str = "127.0.0.1"
    port: str = "8000"


class ProjectSettings(BaseSettings):
    """Represents Project settings"""

    class Config:
        env_prefix = "SETTINGS_"

    base_dir: str = os.path.dirname(os.path.abspath(__file__))
    project_name: str = "parser"
    log_file: bool = False


class Settings(BaseSettings):
    database: DB = DB()
    api: UvicornURL = UvicornURL()
    project: ProjectSettings = ProjectSettings()
    redis: Redis = Redis()
    celery: Celery = Celery()
    rabbit: RabbitMQ = RabbitMQ()


@lru_cache
def get_settings() -> Settings:
    """Singleton"""
    return Settings()


settings = get_settings()
