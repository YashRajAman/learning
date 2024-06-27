from sqlalchemy import Column, Integer, String, Float
from database import Base

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    author = Column(String, index=True)
    isbn = Column(String, nullable=True)
    price = Column(Float, nullable=True)
