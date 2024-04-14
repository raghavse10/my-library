from datetime import datetime, timedelta

from fastapi import APIRouter, Depends

from controller.circulation import controller_book_checkout, controller_book_return
from schema.requests import CheckoutRequest, ReturnRequest

router = APIRouter(
    tags=["Circulation"],
    responses={404: {"description": "Not found"}},
)


@router.post("/book-checkout")
async def book_checkout(request: CheckoutRequest):
    try:
        return await controller_book_checkout(request)
    except Exception as e:
        return f"Exception occurred: {str(e)}"


@router.post("/book-return")
async def book_return(request: ReturnRequest):
    try:
        return await controller_book_return(request)
    except Exception as e:
        return f"Exception occurred: {str(e)}"


