from app import pun_bot
from flask import request, jsonify



# @pun_bot.route('/')
# @pun_bot.route('/index')
#
# def index():
#     return "Hello, World!"
#
# @pun_bot.route('/hello/<name>')
# def hello(name):
#     return ('Hello, %s' % name)
#
# @pun_bot.route('/loves/<first>/<second>')
# def loves(first, second):
#     return '%s loves %s!' % (first, second)
#
# @pun_bot.route('/weather')
# def weather():
#     umbrella = request.args('umbrella')
#     return 'OP'

@pun_bot.route('/ack', methods=['POST'])
def ack():
    message = {
        'author': 'ACK bot',
        'text': f'I got your message',
    }
    return jsonify(message)

@pun_bot.route('/', methods=['POST'])
def respond():
    # data = request.get_json()
    # params = data.get('params', {})
    # topic = params.get('topic', '')

    message = {
        'author': 'Pun Bot',
        'text': 'I like to make punny funs',
    }
    return jsonify(message)
