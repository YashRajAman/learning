def test_conn(conn):
    if conn:
        print("Got connection.")
        test_query = "select * from user_details where user_id=(select user_id from user_authentication where username='first_user')"
        cur = conn.cursor()
        cur.execute(test_query)
        result = cur.fetchone()
        print(result)
        print("Connection working.")
        cur.close()
        return True
    else:
        return False