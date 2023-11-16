import os

from celery import Celery

from app.settings.settings import settings

celery = Celery(
    'worker',
    backend=f"redis://{settings.redis.host}:{settings.redis.port}/{settings.redis.db}",
    broker=f"amqp://{settings.rabbit.username}:{settings.rabbit.password}"
           f"@{settings.rabbit.host}:{settings.rabbit.port}//")
