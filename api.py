import connector
from constants import *
from flask import Flask, request, render_template
from flask_restful import Api, resource
from flask_cors import CORS
from controllers import
from models import

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SECRET_KEY']
