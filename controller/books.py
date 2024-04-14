from datetime import datetime, timedelta
from database.connection import database
from schema.response import response


async def controller_view_all_books():
    result = await database.books.find({}, {'_id': 0}).to_list(None)
    return response(result, 200, "All books displayed successfully", False)


