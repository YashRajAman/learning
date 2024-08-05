from pydantic import BaseModel
from typing import Optional



class ReqUser(BaseModel):
    id : Optional [int] = None
    name: str
    UUID: Optional [str] = None
    phone: str
    email: str
    address: Optional [str] = None

    class Config:
        from_attributes = True




class ResUser(BaseModel):
    id : Optional [int] = None
    UUID: Optional [str] = None
    address: Optional [str] = None
    name: str = None
    phone: str = None
    email: str = None
    

    class Config:
        from_attributes = True
        exclude_none = True

class UpdateReUser(BaseModel):
    id : Optional [int] = None
    UUID: Optional [str] = None
    name: Optional [str] = None
    phone: Optional [str] = None
    email: Optional [str] = None
    address: Optional [str] = None

    class Config:
        from_attributes = True
        exclude_none = True