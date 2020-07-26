import json
import uuid

from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields
from flask_restplus import reqparse
from flask_restplus import abort
from flask_restplus import marshal_with

api = Namespace('users', description='API de usuarios')

user = {
    'id': fields.String(required=True, description='Identificador'),
    'username': fields.String(required=True, description='Usuário'),
    'email': fields.String(required=True, description='Email'),
    'first_name': fields.String(required=True, description='Primeiro Nome'),
    'last_name': fields.String(required=True, description='Último Nome'),
    'individual_registration': fields.String(required=True, description='CPF'),
    'birth_date': fields.Date(required=True, description='Data de Nascimento'),
    'password': fields.String(required=True, description='Senha'),
}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('email', type=str)
parser.add_argument('first_name', type=str)
parser.add_argument('last_name', type=str)
parser.add_argument('individual_registration', type=str)
parser.add_argument('birth_date', type=str)
parser.add_argument('password', type=str)

@api.route('/')
class UserListAPI(Resource):
    @marshal_with(user)
    def get(self):
        pass