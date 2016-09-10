import connector
from constants import *
from flask import Flask, request, render_template
from flask_restful import Api, Resource
from flask_cors import CORS
from controllers import questionController, userController
from models import documents, embedded_documents

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['SECRET_KEY']

api.add_resource(userController.UserController,'/api/users')
api.add_resource(userController.CredentialController, '/api/updatePassword')
api.add_resource(userController.LogInController, '/api/login')


api.add_resource(questionController.AskQuestionController, '/api/askQuestion')
api.add_resource(questionController.AnswerQuestion, '/api/answerQuestion')

if __name__ == '__main__':
    app.run(debug=True)
