from sqlite3 import connect
from dotenv import load_dotenv
from os import getenv

load_dotenv()
db_path = getenv('DB_PATH')
def confirm_db():
    with connect(db_path) as app_conn:
        print(f'{type(app_conn)} database exists and is loaded')