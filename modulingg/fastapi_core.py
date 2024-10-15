import os
import sys
from fastapi import FastAPI
from modulingg.controllers.autoload import autoload_modules, get_router_endpoints, mono_module_run
from modulingg.controllers.config import CONFIGURATION
from modulingg.core.internal_router import load_internal_router
from modulingg.schemas.basic_response import HostResponse, ModulesListResponse

app = FastAPI()
fastapi_status = os.getenv("FASTAPI_STATUS", "multi_module") 

if CONFIGURATION['enable_internal_router']:
    load_internal_router(app)

if fastapi_status == "mono_module":
    fastapi_monomodule = os.getenv("FASTAPI_MODULE")
    mono_module_run(app, fastapi_monomodule)
elif fastapi_status == "inspector":
    inspector_module = os.getenv("FASTAPI_MODULE")
    endpoints = get_router_endpoints(app, inspector_module)
    sys.exit(0)
else:
    autoload_modules(app)
