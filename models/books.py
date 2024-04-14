from pydantic import BaseModel


class Books(BaseModel):
    BookID: int
    BookName: str
    NumberOfCopies: int

