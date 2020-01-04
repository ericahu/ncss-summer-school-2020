from flask import Flask

pun_bot = Flask(__name__)

from app import routes
