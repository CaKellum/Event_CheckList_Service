''' this file will contain function that are useful to all the resources '''
from flask_restful import abort

def abort_if_item_doesnt_exist(id, item_type):
    abort(404, message = f"{item_type} with identifier {id} doesn't exist")