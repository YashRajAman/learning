import traceback
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from typing import Optional
from datetime import UTC
import db_actions.user_auth_dao as auth

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
SECRET_KEY = "WHOTHEFUCKAREYOU?"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC)  + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None


def validate_token(token: str, db):
    try:
        data = decode_access_token(token)
        if data:
            user_data = auth.validate_user(data["username"], data["password"], db)
            return user_data
        else:
            return None
    
    except Exception as e:
        traceback.print_exc()
        return None
        