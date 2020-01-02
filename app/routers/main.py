from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
async def read_users():
    return [{"ok"}]
