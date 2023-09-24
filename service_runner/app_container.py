''' This file creates and adds the routes and resources to the app and api '''
from flask import Flask
from flask_restful import Api
from os import getenv
from . import database_mgr

app = Flask(__name__)
api = Api(app)

from .routes import routes
from . import resources
routes.loaded_indicator()


def run():
    ''' This is the function that will run the app via the cli'''
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    database_mgr.start_db()
    app.run()
