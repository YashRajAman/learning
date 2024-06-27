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