from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v2')
async def read_root():
    return {"message": "Test Module v2"}