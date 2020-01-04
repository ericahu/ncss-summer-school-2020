from app import flask_app
from flask import request

@flask_app.route('/')
@flask_app.route('/index')

def index():
    return "Hello, World!"

@flask_app.route('/hello/<name>')
def hello(name):
    return ('Hello, %s' % name)

@flask_app.route('/loves/<first>/<second>')
def loves(first, second):
    return '%s loves %s!' % (first, second)

@flask_app.route('/weather')
def weather():
    umbrella = request.args('umbrella')
    return 'OP'
