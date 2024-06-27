from pydantic import BaseModel

class BookSchema(BaseModel):
    id: int
    name: str
    author: str
    isbn: str = None
    price: float = None

    class Config:
        orm_mode = True
