''' creates the service class '''
from sqlalchemy import Column, Integer, String, ForeignKey, Table, true
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database_mgr import db
from .equipment import Equipment


association_table = Table("service_equipment", 
                          db.Model.metadata, 
                          Column("service_id", ForeignKey("service.id"), primary_key=True),
                          Column("equipment_id", ForeignKey("equipment.id"), primary_key=True))

class Service(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    equipment: Mapped[list[Equipment]] = relationship(secondary=association_table)

    def update(self, service):
        self.name = service.name
        self.equipment = service.equipment
