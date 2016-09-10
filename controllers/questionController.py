from __init__ import *
from auth import auth

class AskQuestionController(Resource):

    @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question', required=True, help='Please specify Question')
        args = parser.parse_args()
        question = documents.Question()
        question.question = args['question']
        question.questionUser = g.user
        return {'response':'Success'}

class AnswerQuestion(Resource):

    @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('questionId', required=True, help='Please specify questionId')
        parser.add_argument('answer', required=True, help='Please specify Answer')
        args = parser.parse_args()
        questionToBeAnswered = documents.Question.objects(id=args['questionId']).first()
        if questionToBeAnswered is None:
            return {'response':'Invalid questionId'},400
        answerOfQuestion = embedded_documents.Answer()
        answerOfQuestion.answer = args['answer']
        answerOfQuestion.answerUser = g.user
        questionToBeAnswered.answers.append(answerOfQuestion)
        return {'response':'Success'}

    @auth.login_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('questionId', required=True, help='Please specify questionId')
        args = parser.parse_args()
        question = documents.Question.objects(id=args['questionId']).first()
        if question is None:
            return {'response':'Invalid questionId'},400
        answerDataDict = []
        for answer in question.answers:
            answerDict = {}
            answerDict['username'] = answer.answerUser
            answerDict['answer'] = answer.answer
            answerDataDict.append(answerDict)

        return answerDataDict

class AllQuestionsController(Resource):

    @auth.login_required
    def get(self):
        allQuestions = documents.Question.objects()
        allQuestionsDict = []
        for question in allQuestions:
            questionDict = {}
            questionDict['question'] = question.question
            allQuestionsDict.append(questionDict)
        return allQuestionsDict
