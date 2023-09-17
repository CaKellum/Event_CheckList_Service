from ..app_container import api
from flask_restful import Resource

class IndividualEventResources(Resource):
    def get(self, event_id):
        pass
    
    def delete(self, event_id):
        pass

    def put(self, event_id):
        pass


class ListEventsResource(Resource):
    def get(self):
        pass

    def post(self):
        pass


api.add_resource(IndividualEventResources, '/event/<event_id>')
api.add_resource(ListEventsResource, '/events')