from tempfile import tempdir
from flask import Flask
from flask_cors import CORS
from os import path, environ, pardir

flask_app = Flask(__name__, static_folder="../../static", template_folder="../../templates")
#CORS(flask_app, resources={r"/*": {"origins": "*"}})
flask_app.config.from_object('app.config')

# This block will override configurations that have matching environment variables if the config.py
# file allows it.
if flask_app.config['OVERRIDE_FROM_ENVIRONMENT_VARIABLES']:
    for conf_key in flask_app.config:
        if conf_key in environ:
            flask_app.config[conf_key] = environ[conf_key]

APP_PATH = path.abspath(path.join(path.join(path.dirname(__file__), '..'), '..'))
flask_app.config['APP_PATH'] = APP_PATH
