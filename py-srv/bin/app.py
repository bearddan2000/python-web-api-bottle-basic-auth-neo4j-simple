from bottle import auth_basic, route, run

import logging
from model import DbModel

logging.basicConfig(level=logging.INFO)

neo = DbModel()

def is_authenticated_user(user, password):
    # You write this function. It must return
    # True if user/password is authenticated, or False to deny access.
	if user == 'user' and password == 'pass':
		return True
	return False

@route('/')
def smoke_test():
    cipher = 'UNWIND range(1, 3) AS n RETURN n, n * n as n_sq'
    d = neo.connect().run(cipher).data()
    return {'results': d}

@route('/dog')
@auth_basic(is_authenticated_user)
def get_all():
    return neo.get_all()

@route('/dog/name/<name>')
@auth_basic(is_authenticated_user)
def filter_by_name(name: str):
    return neo.filter_by_name(name)

@route('/dog/breed/<breed>')
@auth_basic(is_authenticated_user)
def filter_by_breed(breed: str):
    return neo.filter_by_breed(breed)

@route('/dog/color/<color>')
@auth_basic(is_authenticated_user)
def filter_by_color(color: str):
    return neo.filter_by_color(color)

run(host='0.0.0.0', port=8000,debug=True)
