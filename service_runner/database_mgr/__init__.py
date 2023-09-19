from sqlite3 import Connection, connect
from dotenv import load_dotenv
from os import getenv, path

load_dotenv()
db_path = getenv('DB_PATH')
table_file_path = getenv('TABLE_PATH')

def confirm_db():
    should_load_tables = (path.exists(db_path) == False)
    with connect(db_path) as app_conn:
        if should_load_tables:
            print("loading the tables")
            load_file(app_conn)
        else:
            print("db file existed")

def load_file(app_conn: Connection):
    with open(table_file_path) as file: 
        sql_script = file.read()
        with app_conn.cursor() as cursor:
            cursor.executescript(sql_script)