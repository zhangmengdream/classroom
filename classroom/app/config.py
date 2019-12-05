import os

UPLOAD_PATH_IMAGE = os.path.join(os.path.dirname(__file__), 'static/images')
UPLOAD_PATH_VIDEO = os.path.join(os.path.dirname(__file__), 'static/videos')

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/classroom'
SECRET_KEY = 'HADIUHDASD34EWhuiH89nuHu-0i0IjoKPkhjioh900jsdioPj9ojmz09uiAZM8'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
