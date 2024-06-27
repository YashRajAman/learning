import sys
sys.path.append('/home/yash/MyWorkSpace/learning/python3')
from config import SQLALCHEMY_DATABASE_URL

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base

# Database connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Base class for ORM models
Base = declarative_base()

# Define a table as a class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert a new record
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

new_user = User(name='Alita', age=20)
session.add(new_user)
session.commit()


# Query the database
users = session.query(User).all()
for user in users:
    print(user)

# Update a record
user_to_update = session.query(User).filter_by(name='Alice').first()
user_to_update.age = 31
session.commit()

# Delete a record
user_to_delete = session.query(User).filter_by(name='Alice').first()
session.delete(user_to_delete)
session.commit()
