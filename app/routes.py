from app import pun_bot
from flask import request, jsonify

@pun_bot.route('/echo', methods=['POST'])
def word_count():
  # Get the message data
  data = request.get_json()
  author = data.get('author', 'I don\'t know your name')
  text = data.get('text', '')

  # Create a message to send to the sorted
  message = {
    'author': 'Echo bot',
    'text': f'{author} said: {text}',
  }

  # Return the JSON
  return jsonify(message)

@pun_bot.route('/ack', methods=['POST'])
def ack():
    person = request.get_json()
    print(person)
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

# Responds to "How do I contribute / add a pun?"
@pun_bot.route('/contribution', methods=['POST'])
def contribution():
    message = {
        'author': 'Pun Bot',
        'text': 'You can add your punny puns here! --> TODO'
    }
    return jsonify(message)




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
