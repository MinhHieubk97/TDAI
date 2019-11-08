from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_restful import Api

from server.config import config_by_name

mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    initialize_extensions(app)

    register_router(app)

    return app


def initialize_extensions(app):
    mongo.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


def register_router(app):
    api = Api(app)
    from server.controllers.user_controller import UserController_Register

    api.add_resource(UserController_Register, '/users/register')
    api.add_resource(UserController_Register, '/users/login')
