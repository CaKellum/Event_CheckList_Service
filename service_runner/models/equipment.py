''' Creates the equipment class'''


class Equipment():
    def __init__(self, id, equip_name, amt):
        self.id = id
        self.equip_name = equip_name
        self.amt = amt

    def update(self, equipment):
        self.equip_name = equipment.equip_name
        self.amt = equipment.amt
