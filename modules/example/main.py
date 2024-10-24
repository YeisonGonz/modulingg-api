from fastapi import APIRouter

router = APIRouter()
from .controllers.controller import test_controller

@router.get('/api')
async def read_root():
    return {"message": "Modulo 1 de la api"}