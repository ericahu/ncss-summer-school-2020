from app import pun_bot
from pun_selector import Pun_Selector

from flask import request, jsonify
import re

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

# Responds to "How do I contribute / add a pun?"
@pun_bot.route('/contribution', methods=['POST'])
def contribution():
    message = {
        'author': 'Pun Bot',
        'text': 'You can add your punny puns here! --> TODO'
    }
    return jsonify(message)

@pun_bot.route('/', methods=['POST'])
def pun_bot():
    data = request.get_json()
    text = data.get('text', '')
    returned_text = _regex_handler(text)

    message = {
        'author': 'Pun Bot',
        'text': returned_text,
    }
    return jsonify(message)

def _regex_handler(text):
    pattern = re.compile('(?i)give me a pun')
    if pattern.match(text):
        ps = Pun_Selector()
        ps.input()
        return ps.random_choice()['Description']
    else:
        return 'I like to make punny funs!'



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
