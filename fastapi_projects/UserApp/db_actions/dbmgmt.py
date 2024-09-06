from unittest import result
import psycopg2
from psycopg2 import pool
import traceback


class dbPool:

    __slots__ = ('host', 'database', '__username', '__password', 'port', 'options', 'conn', 'cursor', 'pool')


    def __init__(self, host, database, user, password, options=None, port=5432):
        self.host = host
        self.database = database
        self.__username = user
        self.__password = password
        self.port = port
        self.options = options
        # self.DSN = f"dbname='{self.database}' user='{self.user}' password='{password}' host='{self.host}' port='{self.port}' options='{self.options}'"
        self.conn = None
        self.cursor = None
        self.pool = None
    
    def create_pool(self):
        try:
            self.pool = pool.SimpleConnectionPool(1, 10, user=self.__username, password=self.__password,
                                        host=self.host, port=self.port, database=self.database,
                                        options=self.options)
            print("Pool created")
        except psycopg2.Error as e:
            traceback.print_exc()
            raise Exception(mesage="Error in database pool creation.")
    
    def get_conn(self, create_pool=False):
        try:
            if create_pool and self.pool is None:
                self.create_pool()

            if create_pool and self.pool is not None:
                print(f"Connection pool already exists. Skipping pool creation. ")

            
            self.conn = self.pool.getconn()
            if self.conn:
                print("Connection fetched: ", type(self.conn))
                yield self.conn
            else:
                print("Connection not created")
                return None
            
        except Exception as e:
            traceback.print_exc()
            return None
        finally:
            if self.conn:
                self.pool.putconn(self.conn)


    def close_pool(self):
        if self.pool:
            self.pool.closeall()
            self.pool = None
            print("Pool closed")
        else:
            print("Pool is already closed")



    def authenticate(self, username:str = None, password:str = None):
        Result = {"username":False, "password":False}

        if self.__username == username:
            Result =  {"username": True}
        if self.__password == password:
            Result = {"password": True}
        
        return Result
    

    def toString(self):
        return f"Host: {self.host}, Database: {self.database}, Port: {self.port}, Options: {self.options}"
    

    

