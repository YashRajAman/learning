host="localhost"
database="user_application"
schema="application_api"
user='yash'
port=5432
password='whothefuckareyou?'
options = f"-c search_path={schema}"

DSN = f"dbname='{database}' user='{user}' password='{password}' host='{host}' port='{port}' options='{options}'"