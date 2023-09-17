''' creates the events class '''


class Event():
    ''' Event class that stores the event instances '''
    def __init__(self, people: list, services: list):
        self.people = people
        self.services = self.services

    def update(self, event):
        self.people = event.people
        self.services = event.services
