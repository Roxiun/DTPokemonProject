import os
class Config(object):
    SECRET_KEY = os.urandom(32)
    #app.config['SECRET_KEY'] = SECRET_KEY