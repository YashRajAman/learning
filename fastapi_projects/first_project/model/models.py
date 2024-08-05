from ast import Name
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from database import engine
from schema.schemas import ReqUser
import service.services as services

SUPER = declarative_base()

class User(SUPER):

    __tablename__= "users"
    __table_args__ = {'schema': 'anime'} 
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    UUID = Column(String, index=True, nullable=False, unique=True)
    name = Column(String, index=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)

    def __init__(self, tuser:ReqUser=None):

        if tuser is not None:
            self.id = tuser.id
            self.name = tuser.name
            self.UUID = services.generate_fixed_length_uuid() if tuser.UUID is None else tuser.UUID
            self.phone = tuser.phone
            self.email = tuser.email
            self.address = tuser.address

SUPER.metadata.create_all(engine)