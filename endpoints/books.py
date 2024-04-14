from controller.books import controller_view_all_books
from fastapi import APIRouter


router = APIRouter(
    tags=["Books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/view-all-books")
async def view_all_books():
    try:
        return await controller_view_all_books()
    except Exception as e:
        return f"Exception occurred: {str(e)}"


