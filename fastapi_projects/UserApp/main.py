import traceback
from fastapi import FastAPI, Depends
import jwt
from schemas.auth_user_schema import create_user_req, user_token_req
from db_actions.db_pools import get_conn
from db_actions import user_auth_dao as auth_dao
from utilities import jwt_auth
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn

# from db_actions.test_conn import test_conn

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
@app.post("/createuser")
def create_user(user:create_user_req, db = Depends(get_conn)):
    try:
        print("Started")
        auth_dao.create_user_auth(user, db)
        print("Done")
        return user
    
    except Exception as e:
        traceback.print_exc()


@app.post("/getusertoken")
def gen_user_token(user: OAuth2PasswordRequestForm = Depends(), db = Depends(get_conn)):
    try:
        print("Generating user token.")

        secret_key = auth_dao.get_user_auth_details(user, db)
        if secret_key is not None:
            token = jwt_auth.create_access_token({"username":user.username, "password":user.password})
            print(f"JWT Token: {token}")

            print(jwt_auth.decode_access_token(token))
            
            return {"access_token": token, "token_type": "bearer"}
        else:
            return {"message":"User verification Failed."}

    except Exception as e:
        traceback.print_exc()
        
@app.post("/validateuser")
def validate_user_token(token: str = Depends(oauth2_scheme), db = Depends(get_conn)):
    try:
        user_data = jwt_auth.validate_token(token,db)
        if user_data is not None:
            user_details = auth_dao.get_user_by_userid(user_data['user_id'], db)
            return user_details
        else:
            return {"message":"Invalid user."}
    except Exception as e:
        traceback.print_exc()

@app.post("/generatefakedata")
def generate_fake_data(token: str = Depends(oauth2_scheme), db = Depends(get_conn)):
    try:
        user_data = jwt_auth.validate_token(token, db)
        if user_data is not None:
            user_id = user_data.get("user_id")
            data = auth_dao.generate_fake_data_by_user_id(user_id, db)
            if data is not None:
                return data
            else:
                return {"Message": f"Error generating data for user_id: {user_id}"}
    

    except Exception as e :
        traceback.print_exc()
        return {"Message": "Error/Exception in generating data."}

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)