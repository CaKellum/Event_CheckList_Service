import pstats
from sqlite3 import Connection, connect

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from os import getenv, path

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

from .. import models

def start_db():
    models.models_loaded()
    db.create_all()