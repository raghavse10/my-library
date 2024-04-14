from pydantic import BaseModel
from datetime import datetime


class Reservation(BaseModel):
    BookID: int
    MemberID: int
    ReservedAt: datetime
    FulfilledAt: datetime | None
