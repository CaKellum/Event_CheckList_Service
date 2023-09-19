from ..app_container import api
from flask_restful import Resource

class IndividualEquipmentResource(Resource):
    def get(self, equip_id):
        pass

    def delete(self, equip_id):
        pass

    def update(self, equip_id):
        pass


class ListEquipmentResource(Resource):
    def get(self):
        pass

    def post(self):
        pass


api.add_resource(IndividualEquipmentResource, '/equipment/<equip_id>')
api.add_resource(ListEquipmentResource, '/equipment')