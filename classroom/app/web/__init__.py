from flask import Blueprint
# 课堂
web = Blueprint('web', __name__)

from app.web import room, auth

