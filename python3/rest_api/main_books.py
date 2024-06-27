from fastapi import FastAPI, Request, Depends
from fastapi.responses import FileResponse
from db_ops import conn_pools
from models import books, Books

app = FastAPI()

BookSchema = books.BookSchema
Books = Books.Books

conn_pools.get_db

@app.get("/")
def introduction():
    intro = "Welcome, this service has many api to manage books' digital record."
    author = "Yash Raj Aman"
    return {"Intro":intro, "Created by": author}

@app.post("/addBook")
def add_book(book: books.BookSchema, db = Depends(conn_pools.get_db)) :
    try:
        print(book)
        oneBook = Books()
        oneBook.name = book.name
        oneBook.author = book.author

        conn = db()
        Books.save(conn)
    except:
        print("What the fuck ?")