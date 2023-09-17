''' creates the person class '''


class Person():
    def __init__(self, id: int, person_name: str):
        ''' initilizer for person '''
        self.id = id
        self.person_name = person_name

    def update(self, person):
        ''' updates the instance '''
        self.person_name = person.name
