from __init__ import *
from auth import auth

class LogInController(Resource):

    @auth.login_required
    def get(self):
        response = {}
        response['id'] = str(g.user.id)
        response['username'] = g.user.username
        response['email'] = g.user.email
        return response


class UserController(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, help='Please specify email')
        parser.add_argument('username', required=True, help='Please specify username')
        parser.add_argument('password', required=True, help='Please specify password')

        args = parser.parse_args()

        if(len(args['password']) < 6 and len(args['password']) > 32):
            return {'response':'Length of password'},403

        user = documents.User()
        user.email = args['email']
        user.username = args['username']
        user.encrypt_password(args['password'])

        user.save()
        userInfo = {}
        userInfo['id'] = str(user.id)
        userInfo['email'] = user.email
        userInfo['username'] = user.username

        return userInfo

class CredentialController(Resource):

    @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('old_password', required=True, help='Please specify old password')
        parser.add_argument('new_password', required=True, help='Please specify new password')
        args = parser.parse_args()

        if(g.user.verify_password(args['old_password'])):
            g.user.encrypt_password(args['new_password'])
            g.user.save()
            return {'response':'Success'}

        return {'response':'Unauthorized'},401

#class EmailVerificationController(Resource):
