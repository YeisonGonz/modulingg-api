from fastapi import APIRouter
from modulingg.controllers.autoload import search_modules

router = APIRouter()

@router.get('/')
async def main():
    return {"message": "Modulingg say Hello!"}

@router.get('/modules')
async def modules():
    return search_modules()

@router.get('/health')
async def health():
    return {"status": "healthy"}

@router.get('/healthcheck')
async def health():
    return {"status": "healthy"}

def load_internal_router(app):
    app.include_router(router)
