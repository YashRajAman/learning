import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import traceback
from database import get_db, engine, Base
from models import Books
from schemas import BookSchema

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log to this file
    level=logging.DEBUG,  # Log all levels (DEBUG and above)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/getBook/{book_id}", response_model=BookSchema)
def get_book(book_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching book with ID {book_id}")
    book = db.query(Books).filter(Books.id == book_id).first()
    if book is None:
        logger.warning(f"Book with ID {book_id} not found")
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/addBook")
def add_book(book: BookSchema, db: Session = Depends(get_db)):
    try:
        new_book = Books(
            name=book.name,
            author=book.author,
            isbn=book.isbn,
            price=book.price
        )
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        logger.info(f"Added book: {new_book}")
        return {"message": "Book added successfully", "book": new_book}
    except Exception as e:
        logger.error("Error adding book", exc_info=True)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
