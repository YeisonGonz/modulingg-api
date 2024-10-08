
from fastapi import FastAPI
from modulingg.controllers.autoload import autoload_modules
from modulingg.schemas.basic_response import HostResponse, ModulesListResponse

app = FastAPI()
modules_list = autoload_modules(app)

@app.get("/")
async def root():
    return HostResponse()

@app.get('/modules')
async def modules():
    return ModulesListResponse(modules=modules_list)
