from ..app_container import api
from flask_restful import Resource


class IndividualServiceResource(Resource):
    def get(self, serv_id):
        pass

    def put(self, serv_id):
        pass

    def delete(self, serv_id):
        pass

class ListServiceResourece(Resource):
    def get(self):
        pass

    def post(self):
        pass

api.add_resource(IndividualServiceResource,'/service/<serv_id>')
api.add_resource(ListServiceResourece, '/service')