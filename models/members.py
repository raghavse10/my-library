from pydantic import BaseModel


class Members(BaseModel):
    MemberID: int
    MemberName: str
