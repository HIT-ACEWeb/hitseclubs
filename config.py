# --*-- coding : utf=8 --*--
#配置脚本
import os
__author__ = 'voidhug'

class Config:

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'mysql://root:123456@localhost/hitseclubs'

config = {
    'development' : DevelopmentConfig,

    'defalut' : DevelopmentConfig
}