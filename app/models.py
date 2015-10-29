#-*- coding: utf-8 -*-
__author__ = 'voidhug'
from . import db
from flask import url_for

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    #如果设置unique，怎么抛出异常给用户？
    name = db.Column(db.VARCHAR(100), nullable=True)
    password = db.Column(db.VARCHAR(100), nullable=True)

    def to_json(self):
        json_users = {
            'name': self.name,
            'password': self.password
        }
        return json_users