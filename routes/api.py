from fastapi import APIRouter
from endpoints import books, members, circulation

router = APIRouter()
router.include_router(books.router)
router.include_router(members.router)
router.include_router(circulation.router)
