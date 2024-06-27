import sys
sys.path.append('/home/yash/MyWorkSpace/learning/python3')
from config import SQLALCHEMY_DATABASE_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,  # Number of connections to keep in the pool
    max_overflow=20,  # Number of connections to create beyond the pool_size
    pool_timeout=30,  # Seconds to wait before giving up on getting a connection from the pool
    pool_recycle=1800,  # Connections older than this many seconds will be recycled
)


# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()