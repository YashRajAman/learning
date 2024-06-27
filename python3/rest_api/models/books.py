from pydantic import BaseModel
from typing import Optional

class BookSchema(BaseModel):
    id: Optional[int] = None
    name: str
    isbn: str
    author: str
    price: float

    class Config:
        from_attributes = True

class ResponseBookSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    isbn: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None
