from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            first_name=data['first_name'],
            second_name=data['second_name'],
            phone_number=data['phone_number'],
            password=data['password'],
        )
        save_changes(new_user)
        response = {
            'status': 'success',
            'message': 'User successfully registered.'
        }
        return response, 201
    else:
        response = {
            'status': 'fail',
            'message': 'Another user with the same email exists',
        }
        return response, 409


def get_all_users():
    return User.query.all()


def get_a_user(user_id):
    return User.query.filter_by(id=user_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()