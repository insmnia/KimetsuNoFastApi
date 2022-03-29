from fastapi import FastAPI

from app.api.v1.api import router as api_router
from app.core.config import get_settings
from app.db.mongodb_utils import connect, close_connection
from app.core.middleware import MaintainceModeMiddleware, SentryMiddleware
from app.core.errors import unauthorized_exception_handler

app = FastAPI(title="KimetsuNoFastApi", debug=True)
settings = get_settings()


app.add_event_handler('startup', connect)
app.add_event_handler('shutdown', close_connection)

app.add_middleware(MaintainceModeMiddleware)
app.add_middleware(SentryMiddleware)
app.exception_handler(unauthorized_exception_handler)

app.include_router(api_router, prefix="/api")
