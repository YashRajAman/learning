from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Books(Base):
    __tablename__ = 'Books'

    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String)
    isbn = Column(String)
    author = Column(String)
    price = Column(Float)

    def __repr__(self):
        return f"Book(id={self.id}, name='{self.name}', isbn='{self.isbn}', author='{self.author}', price={self.price})"

    def save(self, session):
        session.add(self)
        session.commit()

    @classmethod
    def get_by_id(cls, session, book_id):
        return session.query(cls).filter_by(id=book_id).first()

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    def update(self, session, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()