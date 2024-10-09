from fastapi import APIRouter

router = APIRouter()

@router.get('/api')
async def read_root():
    return {"message": "Modulo 1 de la api"}