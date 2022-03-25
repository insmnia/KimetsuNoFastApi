from .main import app
from fastapi import Request

@app.middleware('http')
async def maintaince_mod(request: Request, call_next):
    with open('maintaince.txt','r') as f:
        on = bool(int(f.read()))
        print(on)
    if on:
        return {'Maintaince':'Sorry... We now on maintaince mod'}
    return call_next(request)