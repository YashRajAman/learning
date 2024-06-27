import psycopg2

conn = psycopg2.connect(host="localhost",user="yash",password='whothefuckareyou?',database='development')

if conn:
    print("Yay")
    cursor = conn.cursor()
    cursor.execute("select * from anime.konosuba")
    result = cursor.fetchall()
    for row in result:
        print(row)
else:
    print("l mera")



conn.close()