from fastapi import FastAPI
from .routers import get_routers


def app_factory():
    app = FastAPI()
    for router in get_routers():
        app.include_router(
            router,
            prefix="/api/v1")
    return app
