from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth_user_schema import create_user_req, user_token_req
from utilities.gen_userid import getUserId
from psycopg2.extras import NamedTupleCursor, RealDictCursor
import traceback
from utilities import jwt_auth, generate_fake_data

def create_user_auth(user:create_user_req, conn):
    try:
        ins_query = "insert into user_authentication(user_id, username, password, secret_key) values(%s,%s,%s,%s);"
        if user.user_id is None:
            user.user_id=getUserId()
        cursor = conn.cursor()
        cursor.execute(ins_query, (user.user_id, user.username, jwt_auth.get_password_hash(user.password), user.secret_key))
        conn.commit()
        cursor.close()
        return user.userid
    except Exception as e:
        traceback.print_exc()
        return None


def get_user_auth_details(user: OAuth2PasswordRequestForm, conn):
    try:
        print("Fetching user using username and password")
        fetch_query = "select user_id, username, password, secret_key from user_authentication where username=%s"
        cursor = conn.cursor(cursor_factory=NamedTupleCursor)
        cursor.execute(fetch_query, (user.username,))
        result = cursor.fetchone()

        
        if jwt_auth.verify_password(user.password, result.password):

            if result:
                secret_key = result.secret_key
            conn.commit()
            cursor.close()
            return secret_key
        
        else:
            return None
        
    except Exception as e:
        traceback.print_exc()
        return None
    
def validate_user(username: str, password: str, conn):
    try:
        print("Validating User.")
        fetch_query = "select user_id, username, password, secret_key from user_authentication where username=%s"
        cursor = conn.cursor(cursor_factory=NamedTupleCursor)
        cursor.execute(fetch_query, (username,))
        result = cursor.fetchone()
        
        if jwt_auth.verify_password(password, result.password):
            return {"user_id":result.user_id, "username":result.username, "secret_key":result.secret_key}
        else:
            return False

    except Exception as e:
        traceback.print_exc()
        return False


def get_user_by_userid(user_id, conn):
    try:
        sql_query = "select user_id, name, contact, email, address, occupation, hobby, highest_qualification from user_details where user_id=%s"
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        print(user_id)
        cursor.execute(sql_query, (user_id,))
        result = cursor.fetchone()
        print(result)
        return result
    except:
        traceback.print_exc()

def generate_fake_data_by_user_id(user_id, conn):
    try:
        fake_object = generate_fake_data.fake_data(user_id)
        fake_data = list(fake_object.get_full_data().values())
        insert_sql = """insert into user_details (user_id, name, contact, email, address, occupation, hobby, highest_qualification)
                        values (%s,%s,%s,%s,%s,%s,%s,%s)"""
    
        cursor = conn.cursor()
        cursor.execute(insert_sql, fake_data)

        conn.commit()
        cursor.close()

        return fake_data    
    
    except Exception as e:
        traceback.print_exc()
        return None