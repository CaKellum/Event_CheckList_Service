''' Creates the equipment class'''
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database_mgr import db

class Equipment(db.Model):
    def __init__(self, id: int, equip_name: str, amt: int):
        self.id = id
        self.equip_name = equip_name
        self.amt = amt

    def update(self, equipment):
        self.equip_name = equipment.equip_name
        self.amt = equipment.amt
