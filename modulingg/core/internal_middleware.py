from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class RequestInfoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Get request information
        request_info = {
            "ip": request.client.host,
            "method": request.method,
            "url": str(request.url),
            "params": dict(request.query_params)
        }

        response = await call_next(request)
        return response