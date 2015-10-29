#!usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'voidhug'

import os
from app import create_app, db
from flask.ext.script import Manager, Shell
from app.models import Users

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, Users=Users)
manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()

