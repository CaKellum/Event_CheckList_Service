''' creates the person class '''
from socket import AI_V4MAPPED
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database_mgr import db

class Person(db.Model):
    def __init__(self, id: int, person_name: str):
        ''' initilizer for person '''
        self.id = id
        self.person_name = person_name

    def update(self, person):
        ''' updates the instance '''
        self.person_name = person.name


class EventPerson(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    person_id: Mapped[Person] = mapped_column(ForeignKey("person.id"))
    person = relationship(Person)


