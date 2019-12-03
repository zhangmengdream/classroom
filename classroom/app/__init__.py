from flask import Flask
from app.models.base import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    db.init_app(app)
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.room import web
    from app.web.auth import auth
    app.register_blueprint(web)
    app.register_blueprint(auth)
