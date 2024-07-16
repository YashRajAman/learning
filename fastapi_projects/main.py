import traceback
import database
from sqlalchemy.orm import Session
from model.models import User
from schema.schemas import ReqUser, ResUser, UpdateReUser
from fastapi import FastAPI, Depends
import uvicorn


app = FastAPI()



@app.get("/")
def introduction():
    return {"Message": "Hi there, this application handles user operations using API calls."}


@app.post("/adduser")
def add_user(reqUser: ReqUser, db: Session = Depends(database.get_db)):
    try:
        oneUser = User(reqUser)
        db.add(oneUser)
        db.flush()
        db.commit()
        response = ResUser.model_validate(oneUser)
        return response
    
    except Exception as e:
        return {"Exception": traceback.format_exc()}


@app.get("/getalluser")
def getallusers(db: Session = Depends(database.get_db)):
    try:
        Users = db.query(User).all()
        for user in Users:
            print(user)
        response = [ResUser.model_validate(oneUser) for oneUser in Users]
        return response
    except Exception as e:
        return {"Exception": traceback.format_exc()}
    





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)