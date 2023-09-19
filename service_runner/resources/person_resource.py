from ..app_container import api
from flask_restful import Resource

class IndividualPersonResource(Resource):
    def get(self, person_id):
        pass

    def delete(self, person_id):
        pass

    def put(self, person_id):
        pass

class ListPersonResource(Resource):
    def get():
        pass

    def post():
        pass

api.add_resource(IndividualPersonResource, '/person/<person_id>')
api.add_resource(ListPersonResource, '/people')