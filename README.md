# Basic-Flask-restplus-api

*Installation*

- Clone this repo
- Install the requirements using the command `pip3 install requirements.txt`

To run
 - `python3 manage.py run` for the server
 - `python3 manage.py tests` for tests
 
 *Endpoints*
 
 - GET `/users/` - list all registered users
 - GET `/users/<int::user_id>` - get a specific user
 - POST `/users/` - register a new user with the data in the following format

      {

        "email": "string",

        "first_name": "string",

        "second_name": "string",

        "phone_number": "string",

        "password": "string"

      }
