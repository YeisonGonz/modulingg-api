import os
import sys
from fastapi import FastAPI

from modulingg.controllers.config import CONFIGURATION
from modulingg.controllers.logger import endpoints_print
from modulingg.core.internal_router import load_internal_router
from modulingg.schemas.basic_response import HostResponse, ModulesListResponse
from .controllers.autoload import Autoloader 

app = FastAPI()
fastapi_status = os.getenv("FASTAPI_STATUS", "multi_module")

autoloader = Autoloader()

if CONFIGURATION['enable_internal_router']:
    load_internal_router(app)

if fastapi_status == "mono_module":
    fastapi_monomodule = os.getenv("FASTAPI_MODULE")
    autoloader.mono_module_run(app, fastapi_monomodule)
elif fastapi_status == "inspector":
    inspector_module = os.getenv("FASTAPI_MODULE")
    endpoints = autoloader.get_router_endpoints(app, inspector_module)
    endpoints_print(endpoints,inspector_module)
    sys.exit(0)
else:
    autoloader.autoload_modules(app)
