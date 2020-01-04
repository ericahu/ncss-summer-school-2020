from app import pun_bot
from flask import request

@pun_bot.route('/')
@pun_bot.route('/index')

def index():
    return "Hello, World!"

@pun_bot.route('/hello/<name>')
def hello(name):
    return ('Hello, %s' % name)

@pun_bot.route('/loves/<first>/<second>')
def loves(first, second):
    return '%s loves %s!' % (first, second)

@pun_bot.route('/weather')
def weather():
    umbrella = request.args('umbrella')
    return 'OP'
