''' creates the events class '''
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database_mgr import db

class Event(db.Model):
    ''' Event class that stores the event instances '''
    def __init__(self, people: list, services: list):
        self.people = people
        self.services = self.services

    def update(self, event):
        self.people = event.people
        self.services = event.services
