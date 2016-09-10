from __init__ import *

auth = HTTPBasicAuth()

@auth.verify_password()
def verify_password(username, password):
    user = documents.User.objects(username=username).first()
    if user is None:
        return False
    if user.verify_password(password) == False:
        return False
    g.user = user
    return True
