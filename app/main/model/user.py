from .. import db
import re
from sqlalchemy.orm import validates 

class User(db.Model):
    """ A class representing the user model """
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    second_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address') 
        return email

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) < 6 or not phone_number.isdigit():
            raise AssertionError('The phone number is not valid')
        return phone_number

    @validates('password')
    def validate_password(self, key, password):
        if len(password) < 6:
            raise AssertionError('The password is too short')
        return password


