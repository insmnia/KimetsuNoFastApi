from fastapi import FastAPI
from app.api.v1.api import router as api_router

from app.db.mongodb_utils import connect, close_connection

app = FastAPI(title="KimetsuNoFastApi",debug=True)

app.add_event_handler('startup', connect)
app.add_event_handler('shutdown', close_connection)
app.include_router(api_router, prefix="/api")
