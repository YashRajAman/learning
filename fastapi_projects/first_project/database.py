from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://yash:whothefuckareyou?@localhost/development"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
    connect_args={"options": "-csearch_path=anime"},
)

LocalSession = sessionmaker(autocommit=False, autoflush=True, bind=engine)


# Dependency function
def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()