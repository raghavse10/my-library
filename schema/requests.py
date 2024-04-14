from pydantic import BaseModel


class CheckoutRequest(BaseModel):
    BookID: int
    MemberID: int


class ReturnRequest(BaseModel):
    BookID: int
    MemberID: int

