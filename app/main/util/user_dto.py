from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user username'),
        'second_name': fields.String(required=True, description='user password'),
        'phone_number': fields.String(required=True, description='user phone number'),
        'password': fields.String(required=True, description='user password')
    })