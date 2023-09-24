''' creates the person class '''
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database_mgr import db

class Person(db.Model):
    def __init__(self, id: int, person_name: str):
        ''' initilizer for person '''
        self.id = id
        self.person_name = person_name

    def update(self, person):
        ''' updates the instance '''
        self.person_name = person.name
