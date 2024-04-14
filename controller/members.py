from datetime import datetime, timedelta
from database.connection import database
from schema.response import response


async def controller_view_all_members():
    result = await database.members.find({}, {'_id': 0}).to_list(None)
    return response(result, 200, "All members displayed successfully", False)


