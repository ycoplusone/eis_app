import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'eis_app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'qwer1234' # 안키 csrf에 사용된다.

