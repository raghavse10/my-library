from datetime import datetime

from models.reservation import Reservation
from schema.requests import CheckoutRequest


async def handle_reservation(request: CheckoutRequest, now: datetime, database):
    existing_reservation = await database.reservation.find_one({'BookID': request.BookID, 'MemberID': request.MemberID, 'FulfilledAt': None})
    if existing_reservation:
        return "Book already reserved by you."

    reserve_obj = Reservation(**{
        'BookID': request.BookID,
        'MemberID': request.MemberID,
        'ReservedAt': now,
        'FulfilledAt': None
    })
    await database.reservation.insert_one(dict(reserve_obj))
    return "Book not in stock, reservation done!"
