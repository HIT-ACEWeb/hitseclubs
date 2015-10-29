#-*- coding: utf-8 -*-
import os
__author__ = 'voidhug'

class Config:

    #每次请求结束后自动提交数据库中的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'mysql+pymysql://root:admin@localhost/hitseclubs'

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}