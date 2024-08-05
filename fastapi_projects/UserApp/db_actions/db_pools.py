from readline import read_init_file
import psycopg2
from psycopg2 import pool
import db_actions.config as config
import traceback
# psycopg2 connection pool creation

def test_conn(conn, conn_pool):
    if conn:
        print("Got connection.")
        test_query = "select * from user_details where user_id=(select user_id from user_authentication where username='first_user')"
        cur = conn.cursor()
        cur.execute(test_query)
        result = cur.fetchone()
        print(result)
        print("Connection working.")
        cur.close()
        conn_pool.putconn(conn)
        return True
    else:
        return False




conn_pool = pool.SimpleConnectionPool(1, 10, user=config.user, password=config.password,
                                        host=config.host, port=config.port, database=config.database,
                                        options="-c search_path=application_api")

# tconn = conn_pool.getconn()
# if test_conn(tconn, conn_pool):
#     pass
# else:
#     raise Exception("Error database pooling.")
    

def get_conn():
    try:
        print("Taking a connection of pool.")
        conn = conn_pool.getconn()
        if conn:
            yield conn
        else:
            return None
    except Exception as e:
        traceback.print_exc()
    finally:
        print("Putting a connection to pool.")
        conn_pool.putconn(conn)
    


    # if conn_pool:
    #     conn_pool.closeall
    # print("Connections close and resources release.")
