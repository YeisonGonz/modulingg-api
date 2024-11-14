import contextvars
import os
import sys

from fastapi import FastAPI, Request
from modulingg.controllers.config import DynamicConfig
from modulingg.controllers.logger import endpoints_print
from modulingg.core.internal_middleware import RequestInfoMiddleware
from modulingg.core.internal_router import load_internal_router
from .controllers.autoload import Autoloader 

app = FastAPI()
fastapi_status = os.getenv("FASTAPI_STATUS", "multi_module")

config = DynamicConfig()
autoloader = Autoloader()

request_info_var = contextvars.ContextVar("request_info")

app.add_middleware(RequestInfoMiddleware)

if config.get('enable_internal_router'):
    load_internal_router(app)

if fastapi_status == "mono_module":
    fastapi_monomodule = os.getenv("FASTAPI_MODULE")
    autoloader.mono_module_run(app, fastapi_monomodule)
elif fastapi_status == "inspector":
    inspector_module = os.getenv("FASTAPI_MODULE")
    endpoints = autoloader.get_router_endpoints(inspector_module)
    endpoints_print(endpoints,inspector_module)
    sys.exit(0)
else:
    autoloader.autoload_modules(app)
