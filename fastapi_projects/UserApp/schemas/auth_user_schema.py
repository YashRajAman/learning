from pydantic import BaseModel
from utilities import gen_userid
from typing import Optional


class create_user_req(BaseModel):

    user_id: Optional [str] = None
    email: Optional [str] = None
    username: str
    password: str
    secret_key: str

class user_token_req(BaseModel):

    username: str
    password: str

