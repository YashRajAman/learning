from typing import Union
from fastapi import FastAPI
import utilities


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/number/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"number": item_id, "square": utilities.get_squared(item_id)}