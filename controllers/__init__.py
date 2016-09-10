from mongoengine import *
from models import documents
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse
from flask import g, abort
from constants import *
import string
import random
