from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from logging import config as logging_config

from app.settings.logger import LOGGING
from app.settings.settings import get_settings, ProjectSettings, settings

app = FastAPI(
    title=settings.project.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    if settings.project.log_file:
        logging_config.dictConfig(LOGGING)
