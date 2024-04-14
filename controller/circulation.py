from datetime import datetime
from database.connection import database
from helper.circulation import handle_reservation
from models.circulation import Circulation
from schema.requests import CheckoutRequest, ReturnRequest
from schema.response import response


async def controller_book_checkout(request: CheckoutRequest):
    now = datetime.now()
    existing_book = await database.books.find_one({'BookID': request.BookID}, {'BookName': 1, 'NumberOfCopies': 1})
    if not existing_book:
        return response({}, 400, "Book not found!", True)

    existing_checkout = await database.circulation.find_one({'BookID': request.BookID, 'MemberID': request.MemberID, 'ReturnedAt': None})
    if existing_checkout:
        return response({}, 400, "Book already checked out!", True)

    copies = existing_book['NumberOfCopies']
    if copies < 1:
        message = await handle_reservation(request, now, database)
        return response({}, 400, message, True)

    existing_reservations = await database.reservation.find({'BookID': request.BookID, 'FulfilledAt': None}).distinct("MemberID")
    if existing_reservations:
        if request.MemberID not in existing_reservations:
            if copies <= len(existing_reservations):
                return response({}, 400, "Copies already reserved by others!", True)
        else:
            await database.reservation.update_one({'BookID': request.BookID, 'MemberID': request.MemberID}, {'$set': {'FulfilledAt': now}})
    circulation_obj = Circulation(**{
        'BookID': request.BookID,
        'MemberID': request.MemberID,
        'CheckoutAt': now,
        'ReturnedAt': None
    })
    await database.circulation.insert_one(dict(circulation_obj))

    await database.books.update_one({'_id': existing_book['_id']}, {'$set': {'NumberOfCopies': copies - 1}})

    return response({}, 200, f"Checkout successful for book name {existing_book['BookName']}", False)


async def controller_book_return(request: ReturnRequest):
    now = datetime.now()
    existing_checkout = await database.circulation.find_one_and_update({'BookID': request.BookID, 'MemberID': request.MemberID, 'ReturnedAt': None}, {'$set': {'ReturnedAt': now}}, {'_id': 0})
    if not existing_checkout:
        return response({}, 400, "Checkout not found!", True)

    existing_book = await database.books.find_one_and_update({'BookID': request.BookID}, {'$inc': {'NumberOfCopies': 1}}, {'BookName': 1})

    return response({}, 200, f"Return successful for book ID {existing_book['BookName']}", False)

