from datetime import datetime
from pydantic import BaseModel


class Circulation(BaseModel):
    BookID: int
    MemberID: int
    CheckoutAt: datetime
    ReturnedAt: datetime | None

