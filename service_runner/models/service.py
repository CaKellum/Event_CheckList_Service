''' creates the service class '''


class Service():
    def __init__(self, id: int, name: str, equipment: list):
        self.id = id
        self.name = name
        self.equipment = equipment

    def update(self, service):
        self.name = service.name
        self.equipment = service.equipment
