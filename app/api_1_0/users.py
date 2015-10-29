__author__ = 'voidhug'

from flask import jsonify
from . import api
from ..models import Users

@api.route('/users/')
def get_users():
    users = Users.query.first()
    return jsonify(users.to_json())

