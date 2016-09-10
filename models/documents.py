from __init__ import *
from passlib.apps import custom_app_context as pwd_context
from constants import *
from embedded_documents import *
from datetime import *

class User(DynamicDocument):
    username = StringField(unique=True)
    email = StringField(unique=True)
    password = StringField()
    isEmailConfirmed = BooleanField(default=False)

    def encrypt_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

class Question(DynamicDocument):
    question = StringField()
    questionUser = ReferenceField(User, reverse_delete_rule=CASCADE)
    answers = ListField(EmbeddedDocumentField(Answer),default=[])
