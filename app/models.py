#-*- coding: utf-8 -*-
__author__ = 'voidhug'
from . import db

class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    #如果设置unique，怎么抛出异常给用户？
    name = db.Column(db.VARCHAR(100), nullable=True)
    password = db.Column(db.VARCHAR(100), nullable=True)