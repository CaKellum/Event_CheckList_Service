''' Creates the equipment class'''


class Equipment():
    def __init__(self, id, equip_name):
        self.id = id
        self.equip_name = equip_name

    def update(self, equipment):
        self.equip_name = equipment.equip_name
