''' Creates the equipment class'''
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database_mgr import db

class Equipment(db.Model):

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    equip_name: Mapped[str] = mapped_column(String, nullable=False)
    amt: Mapped[int] = mapped_column(Integer, default=0)

    def update(self, equipment):
        self.equip_name = equipment.equip_name
        self.amt = equipment.amt
