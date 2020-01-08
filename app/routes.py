import re
from flask import request, jsonify
from app import pun_bot
from app.pun_selector import Pun_Selector

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
    pattern = re.compile('(?i)gi(ve me|mme) a pun')
    ps = Pun_Selector()
    ps.input()

    if pattern.match(text):
        pun = ps.random_choice()
        formatted = pun['Description']
        if pun['Owner'] != '':
            formatted += f' - {pun["Owner"][0]}'
        return formatted
    # if pattern.match(text):
    #     pun
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
