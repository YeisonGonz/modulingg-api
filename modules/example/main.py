from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1')
async def read_root():
    return {"message": "Test Module v1"}

@router.get('/api/v3')
async def read_root():
    return {"message": "Test Module v1"}