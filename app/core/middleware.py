from fastapi import Request
from fastapi.responses import PlainTextResponse
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint
)
from starlette.responses import Response
import sentry_sdk
from app.core.config import get_settings

settings = get_settings()

sentry_sdk.init(
    "https://0fb68b83d61c410199df65e40a7da001@o1181305.ingest.sentry.io/6294581",
    traces_sample_rate=1.0
)


# noinspection PyTypeChecker
class SentryMiddleware(BaseHTTPMiddleware):
    async def dispatch(
            self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            with sentry_sdk.push_scope() as scope:
                scope.set_context('request', request)
                sentry_sdk.capture_exception(e)
            raise e


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
