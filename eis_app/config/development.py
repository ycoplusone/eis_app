from config.default import *


print('development start')
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'eis_app.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "qwer1234"