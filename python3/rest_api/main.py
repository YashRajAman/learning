from fastapi import FastAPI, Request, Depends
from fastapi.responses import FileResponse
from numeric_calc import math_util as mu
from models import item_base_model as bm
from models import Books

app = FastAPI()



# Simple get with base url
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Multiple path parameter
@app.get("/twoNums/{num1}/{num2}")
def read_two_params(num1: int, num2:int):
    return {"First Number":num1, "Second Number":num2, "Sum":num1+num2, "Product":num1*num2, "x**y":mu.power(num1, num2)}

# Path query parameter
@app.get("/qitems/{item_id}")
def read_qitem(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# The fav icon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")


# Body data without any class 

# Below application is not working as expected
# @app.post("/myanyitemasstring/")
# def get_str_item(item: str):
#     print(item)
#     return {'item':item}

@app.post("/myanyitemasstring/")
async def get_str_item(request: Request):
    body = await request.body()
    return body.decode("utf-8")



# Body data without any class 
@app.post("/mydicitem/")
def get_dict_item(item: dict):
    return item


# Body json data with class
# Item = bm.Item
@app.post("/myitem/")
def create_item(item: bm.Item):
    return item

