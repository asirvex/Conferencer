import unittest
import json
from app.test.base import BaseTestCase


def register_user(self):
    return self.client.post(
        '/users/',
        data=json.dumps(dict(
            email='someone@gmail.com',
            first_name='some',
            second_name='one',
            phone_number='0754525698',
            password='hardpassword'
        )),
        content_type='application/json'
    )

class TestUsers(BaseTestCase):
    def test_registering_new_user(self):
        response = self.client.post(
            '/users/',
            data=json.dumps(dict(
            email='khalid@gmail.com',
            first_name='another',
            second_name='one',
            phone_number='0754525698',
            password='hardpassword'
        )),
        content_type='application/json'
        )

        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data['message'], 'User successfully registered.')


    def test_registering_new_user_invalid_email(self):
        response = self.client.post(
            '/users/',
            data=json.dumps(dict(
            email='khalid.com',
            first_name='another',
            second_name='one',
            phone_number='0754525698',
            password='hardpassword'
        )),
        content_type='application/json'
        )

        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['msg'], 'Error: Provided email is not an email address. ')

    def test_registering_new_user_invalid_phone(self):
        response = self.client.post(
            '/users/',
            data=json.dumps(dict(
            email='khalid@gmail.com',
            first_name='another',
            second_name='one',
            phone_number='sdf',
            password='hardpassword'
        )),
        content_type='application/json'
        )

        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['msg'], 'Error: The phone number is not valid. ')

    def test_registering_new_user_invalid_password(self): 
        response = self.client.post(
            '/users/',
            data=json.dumps(dict(
            email='khalid@gmail.com',
            first_name='another',
            second_name='one',
            phone_number='074542181',
            password='easy'
        )),
        content_type='application/json'
        )

        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['msg'], 'Error: The password is too short. ')

    def test_get_users(self):
        response = self.client.get('/users/')
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_specific_user(self):
        register_user(self)
        response = self.client.get('/users/1')
        response_data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()