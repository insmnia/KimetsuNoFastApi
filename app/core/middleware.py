from fastapi import Request
from fastapi.responses import PlainTextResponse
from starlette.responses import Response

from app.core.config import get_settings
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint
)

settings = get_settings()


class MaintainceModeMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)
        if str(request.url).endswith('admin/'):
            return response
        if settings.MAINTAINCE_MODE:
            return PlainTextResponse(content='Sorry... We now on a maintaince')
        return response
