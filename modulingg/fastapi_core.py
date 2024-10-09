import os
from fastapi import FastAPI
from modulingg.controllers.autoload import autoload_modules, mono_module_run
from modulingg.schemas.basic_response import HostResponse, ModulesListResponse

app = FastAPI()
fastapi_status = os.getenv("FASTAPI_STATUS", "multi_module") 

if fastapi_status == "mono_module":
    fastapi_monomodule = os.getenv("FASTAPI_MODULE")
    mono_module_run(app,fastapi_monomodule)
else:
    autoload_modules(app)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

