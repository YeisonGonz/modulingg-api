from json import loads
from fastapi import Request
from modulingg.controllers.config import DynamicConfig
from modulingg.core.Analytics import Analytics
from starlette.middleware.base import BaseHTTPMiddleware

from modulingg.core.Metrics import MetricManager

metrics = MetricManager()
config = DynamicConfig()

class RequestInfoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Get request information
        request_info = {
            "ip": request.client.host,
            "method": request.method,
            "url": str(request.url),
            "params": dict(request.query_params),
            "headers": dict(request.headers)
        }
        
        if loads(str(config.get('allow_metrics')).lower()): # Use JSON library because, json.loads transform 'false' into False
            metrics.append_metric_value(request_info)     
           
        response = await call_next(request)
        return response