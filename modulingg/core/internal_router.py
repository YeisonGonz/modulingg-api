from fastapi import APIRouter
from modulingg.controllers.autoload import Autoloader
from modulingg.controllers.config import DynamicConfig
from modulingg.core.Analytics import Analytics

autoloader = Autoloader()
router = APIRouter()
config = DynamicConfig()
analytics_obj = Analytics()

modulingg_prefix = config.get('modulingg_prefix')

# Simple internal router with the basic operations

@router.get('/')
async def main():
    return {"message": "Modulingg say Hello!"}

@router.get('/modules')
async def modules():
    return autoloader.search_modules()

@router.get('/health')
async def health():
    return {"status": "healthy"}

@router.get('/healthcheck')
async def health():
    return {"status": "healthy"}

@router.get('/analytics')
async def analytics():
    return analytics_obj.load_analytics().to_string(index=False)


def load_internal_router(app):
    app.include_router(router, prefix=modulingg_prefix)
