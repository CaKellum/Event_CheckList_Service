''' This file creates and adds the routes and resources to the app and api '''
from flask import Flask
from flask_restful import Api
from . import database_mgr

app = Flask(__name__)
api = Api(app)

from .routes import routes
routes.loaded_indicator()


def run():
    ''' This is the function that will run the app via the cli'''
    database_mgr.confirm_db()
    app.run()
