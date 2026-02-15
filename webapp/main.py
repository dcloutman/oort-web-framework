"""
*Warning:* This file belongs to the Oort meta-framework and should not be modified by
 application developers. The contents of this file are subject to change with framework updates.
"""
from oort.util.initialize import flask_app as app
from dotenv import load_dotenv
from os import path, environ, pardir, getenv
from pathlib import Path
import logging
from datetime import datetime
from app.controllers import CONTROLLER_CLASSES
from flask_login import LoginManager
from oort.lib.auth import AuthUser # TODO Move this.
import argparse

env_path = path.join(Path(__file__).resolve().parent.parent, '.env')
load_dotenv(dotenv_path=env_path)

def add_filters():
    import oort.util.templating.filters

def register_controllers():
    for controller_class in CONTROLLER_CLASSES:
        # Registering the base class prevents the helper methods in a patent class from being turned into routes.
        controller_class.register(app, base_class = controller_class.get_base_class())

app.secret_key = getenv('FLASK_SECRET_KEY')
if not app.secret_key:
    raise ValueError("FLASK_SECRET_KEY environment variable is not set. Please set it to a secure value.")

"""
login_manager = LoginManager()
login_manager.init_app(app)

# TODO Move the following somewhere logical
@login_manager.user_loader
def load_user(user_id):
    return AuthUser(user_id)

# End TODO
"""

add_filters()
register_controllers()

if __name__ == '__main__':
    app.run()
