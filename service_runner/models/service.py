''' creates the service class '''
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database_mgr import db


class Service(db.Model):
    def __init__(self, id: int, name: str, equipment: list):
        self.id = id
        self.name = name
        self.equipment = equipment

    def update(self, service):
        self.name = service.name
        self.equipment = service.equipment
