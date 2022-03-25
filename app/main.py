from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from app.api.v1.api import router as api_router

from app.db.mongodb_utils import connect, close_connection

app = FastAPI(title="KimetsuNoFastApi", debug=True)


@app.middleware('http')
async def maintaince_mod(request: Request, call_next):
    response = await call_next(request)
    if str(request.url).endswith('admin/'):
        return response

    with open('maintaince.txt', 'r') as f:
        on = bool(int(f.read()))
    if on:
        return PlainTextResponse(content='Sorry... We now on a maintaince')
    return response


app.add_event_handler('startup', connect)
app.add_event_handler('shutdown', close_connection)
app.include_router(api_router, prefix="/api")
