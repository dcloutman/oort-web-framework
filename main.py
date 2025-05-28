"""
*Warning:* This file belongs to the Oort meta-framework and should not be modified by
 application developers. The contents of this file are subject to change with framework updates.
"""
from oort.util.initialize import flask_app as app
from dotenv import load_dotenv
from os import path, environ, pardir, getenv
import sys
import logging
from datetime import datetime
from app.controllers import controller_classes
from flask_login import LoginManager
from oort.lib.auth import AuthUser # TODO Move this.
import os
import argparse


def add_filters():
    import oort.util.templating.filters

def register_controllers():
    for controller_class in controller_classes:
        controller_class.register(app, base_class = controller_class.get_base_class())

app.secret_key = getenv('FLASK_SECRET_KEY')
if not app.secret_key:
    raise ValueError("FLASK_SECRET_KEY environment variable is not set. Please set it to a secure value.")

login_manager = LoginManager()
login_manager.init_app(app)

# TODO Move the following somewhere logical
@login_manager.user_loader
def load_user(user_id):
    return AuthUser(user_id)

# End TODO

def parse_args():
    parser = argparse.ArgumentParser(description="Oort Development Server")
    parser.add_argument('--host', type=str, default=None, help='Host address')
    parser.add_argument('--port', type=int, default=None, help='Port number')
    return parser.parse_args()

load_dotenv()
add_filters()
register_controllers()

if __name__ == '__main__':
    args = parse_args()
    # Only override if flags are provided, otherwise use .env or Flask defaults
    host = args.host if args.host is not None else None
    port = args.port if args.port is not None else None
    run_kwargs = {}
    if host is not None:
        run_kwargs['host'] = host
    if port is not None:
        run_kwargs['port'] = port
    app.run(**run_kwargs)
