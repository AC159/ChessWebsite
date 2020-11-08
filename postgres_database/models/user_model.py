import os

from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer
from dotenv import load_dotenv

load_dotenv()


# Initializing a JWS object with the secret key and an expiration time:
# Lifetime of the token is 10 minutes.
s = TimedJSONWebSignatureSerializer(os.getenv('APP_SECRET_KEY'), salt='forgot-password', expires_in=600)


class User(UserMixin):
    def __init__(self, username, email, rating, password=None):
        self.id = username
        self.email = email
        self.rating = rating
        self.password = password

    def get_forgot_password_token(self):
        token = s.dumps({'id': self.id}, salt='forgot-password').decode('utf-8')  # The token will contain the user's ID
        return token

    @staticmethod
    def verify_reset_password_token(token):
        try:
            decoded_id = s.loads(token, salt='forgot-password')['id']  # Lifetime of the token is 10 minutes.
        except:
            return None
        return decoded_id
