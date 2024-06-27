import sys
sys.path.append('/home/yash/MyWorkSpace/learning/python3')
from config import SQLALCHEMY_DATABASE_URL

from sqlalchemy import create_engine, text



def get_db_conn():
    """
    This function creates one connection using sql alchemy and returns it.
    """
    global SQLALCHEMY_DATABASE_URL    
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    conn = engine.connect()
    return conn

def get_db_conn_from_pool():
    """
    This function returns a connection from a pool using sqlalchemy.
    """
    global SQLALCHEMY_DATABASE_URL
    engine = create_engine(
                SQLALCHEMY_DATABASE_URL,
                pool_size=10,  # Number of connections to keep in the pool
                max_overflow=20,  # Number of connections to create beyond the pool_size
                pool_timeout=30,  # Seconds to wait before giving up on getting a connection from the pool
                pool_recycle=1800,  # Connections older than this many seconds will be recycled
            )


def execute_query():
    conn = get_db_conn()
    sql_query = text("select * from anime.konosuba")
    result = conn.execute(sql_query)
    for row in result:
        print(row)
    conn.close()



# Using single connection 
execute_query()


