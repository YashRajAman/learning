from fastapi import FastAPI, Depends, Response, HTTPException
from db_ops import conn_pools
from models import books, Books
import traceback
# import logging
import logging.config


# Configure logging
# logging.basicConfig(
#     filename='app.log',  # Log to this file
#     level=logging.DEBUG,  # Log all levels (DEBUG and above)
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )

# logger = logging.getLogger(__name__)


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)



app = FastAPI()


@app.get("/")
def introduction():
    intro = "Welcome, this service has many api to manage books' digital record."
    author = "Yash Raj Aman"
    return {"Intro":intro, "Created by": author}

@app.post("/addBook")
def add_book(book: books.BookSchema, db = Depends(conn_pools.get_db)) :
    try:
        print(book)
        oneBook = Books.BooksModel()
        oneBook.name = book.name
        oneBook.author = book.author
        oneBook.isbn = book.isbn
        oneBook.price = book.price

        print(Books)
        oneBook.save(db)
        return book
    except:
        traceback.print_exc()
        print("What the fuck ?")

@app.post("/getbook")
def get_book(book: books.ResponseBookSchema, db = Depends(conn_pools.get_db)):
    try:
        # logger.info("Starting to get a book using filter.")
        print(book)
        responseEntity = books.ResponseBookSchema()
        response = None
        if book.id:
            # logger.info("Checking with book id.")
            response = db.query(Books.BooksModel).filter(Books.BooksModel.id==book.id).first()
        elif book.name:
            # logger.info("Checking with book name.")
            response = db.query(Books.BooksModel).filter(Books.BooksModel.name==book.name).first()
        elif book.author:
            # logger.info("Checking with book author.")
            response = db.query(Books.BooksModel).filter(Books.BooksModel.author==book.author).first()
        elif book.isbn:
            print(book.isbn)
            # logger.info("Checking with book isbn.")
            response = db.query(Books.BooksModel).filter(Books.BooksModel.isbn==book.isbn).first()

        if response:
            responseEntity.id = response.id
            responseEntity.name = response.name
            responseEntity.author = response.author
            responseEntity.isbn = response.isbn
            responseEntity.price = response.price
        else:
            responseEntity = {"Message":"Book not found with requested details."}
            return responseEntity
        # print(type(response))
        # print(response)

        return responseEntity
    except Exception as e:
        # logger.error(traceback.format_exc())
        traceback.print_exc()
        raise HTTPException(500, detail=str(e))