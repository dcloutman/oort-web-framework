"""
*Warning:* This file belongs to the Oort meta-framework and should not be modified by
 application developers. The contents of this file are subject to change with framework updates.
"""
from oort.util.initialize import flask_app as app
from os import path, environ, pardir
import sys
import logging
from datetime import datetime
from app.controllers import controller_classes
from flask_login import LoginManager
from oort.lib.auth import AuthUser # TODO Move this.


def add_filters():
    import oort.util.templating.filters

def register_controllers():
    for controller_class in controller_classes:
        controller_class.register(app, base_class = controller_class.get_base_class())


login_manager = LoginManager()
login_manager.init_app(app)

# TODO Move the following somewhere logical
@login_manager.user_loader
def load_user(user_id):
    return AuthUser(user_id)

# End TODO

add_filters()
register_controllers()


if __name__ == '__main__':
    app.run()
