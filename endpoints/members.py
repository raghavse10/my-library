from fastapi import APIRouter

from controller.members import controller_view_all_members

router = APIRouter(
    tags=["Members"],
    responses={404: {"description": "Not found"}},
)


@router.get("/view-all-members")
async def view_all_members():
    try:
        return await controller_view_all_members()
    except Exception as e:
        return f"Exception occurred: {str(e)}"


