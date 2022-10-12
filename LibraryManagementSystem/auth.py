'''
import hashlib as hash
import json
class Auth:
    def __init__(self):
        self.salt = "$#@%!"
    def gen_token(self, data):
        comb = data + self.salt
        token = hash.sha1(hash.md5(comb.encode()).hexdigest().encode())
        return token.hexdigest()
    def load_creds(self):
        with open('signup.json', 'r') as handle:
            buff1 = handle.read()

        with open('token.json', 'r') as handle:
            buff2 = handle.read()

        self.sign_data = json.loads(buff1)
        self.token_data = json.loads(buff2)

    def signup(self, user, passw, retype_passw):
        if passw == retype_passw:
            self.load_creds()
            self.sign_data[user] = self.gen_token(passw)

            with open('signup.json', 'w') as handle:
                handle.write(json.dumps(self.sign_data))

            return {"code": 200, "status": "Successfully Signed up"}
        else:
            return {"code": 400, "status": "Mismatch of password"}

    def login(self, user, passw):
        self.load_creds()
        if user in self.sign_data.keys():
            if self.gen_token(passw) == self.sign_data[user]:
                token = self.gen_token(user + passw)
                self.token_data[user] = token
                with open('token.json', 'w') as handle:
                    handle.write(json.dumps(self.token_data))
                return {"code": 200, "auth token": token, "status": "Successfully Logged In"}
            else:
                return {"code": 400, "status": "Invalid Password"}
        else:
            return {"code": 400, "status": "User not signed up"}

    def check_auth(self, user, token):
        self.load_creds()
        if user in self.token_data.keys():
            if self.token_data[user] == token:
                return 200
        else:
            return 400
a = Auth()
print(a.check_auth('arun','ca7a5ad6b79309c5e67a296b6aaf0cc20fc4e059'))
'''
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class Email_OR_Username(BaseBackend):
    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None):
        userModel = get_user_model()
        try:
            user = userModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            if user.check_password(password):
                return user
        except userModel.DoesNotExist:
            return None