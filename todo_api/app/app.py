import logging

from app.apis.v1 import api as v1
from app.config import settings
from app.middleware import setup_cors
from fastapi import FastAPI
from fastapi.routing import APIRoute

logger = logging.getLogger(__name__)


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, 'read_items'


def setup(app_name: str):
    todo_app = FastAPI(title=app_name, openapi_url=settings.OPENAPI_URL)
    setup_cors(todo_app)
    todo_app.include_router(
        v1.router,
        prefix="/v1",
        tags=["v1"],
    )
    use_route_names_as_operation_ids(todo_app)
    return todo_app


app = setup("todo_api")
