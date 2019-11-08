from datetime import datetime

from flask import jsonify

from flask_restful import reqparse, abort, Api, Resource

from server import bcrypt
from server.models.user import User


class UserController_Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()

        first_name = args['first_name']
        last_name = args['last_name']
        email = args['email']
        password = bcrypt.generate_password_hash(args['password']).decode('utf-8')
        created = datetime.utcnow()
        user = User().insert({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'created': created
        })
        return jsonify({'result': user})
