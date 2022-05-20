import datetime

# config Token
DEBUG = True
TESTING = True
PORT = 5001
JWT_SECRET_KEY = "Udemy"
JWT_BLACKLIST_ENABLED = True
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=2)
# JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=15)
