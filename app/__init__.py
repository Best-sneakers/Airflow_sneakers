from logging import config as logging_config

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.settings.logger import LOGGING
from app.settings.settings import settings

app = FastAPI(
    title=settings.project.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.get("/")
async def root():
    return {"message": "Server running"}


@app.on_event("startup")
async def startup():
    if settings.project.log_file:
        logging_config.dictConfig(LOGGING)
