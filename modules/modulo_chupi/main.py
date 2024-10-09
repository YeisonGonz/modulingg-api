from fastapi import APIRouter

from modules.modulo_chupi.database.database import printDatabase

router = APIRouter()

@router.get('/ap2')
async def read_root():
    return {"message": printDatabase()}