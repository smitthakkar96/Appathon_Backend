from __init__ import *
from datetime import datetime

class Answer(EmbeddedDocument):
    answerUser = GenericReferenceField()
    answer = StringField()
    createdAt = DateTimeField(default=datetime.now())
