from tempfile import tempdir
from flask import Flask
from flask_cors import CORS
from os import path, environ, pardir

flask_app = Flask(__name__, static_folder="../../static", template_folder="../../templates")
#CORS(flask_app, resources={r"/*": {"origins": "*"}})

# Set the app path to the root of the application
APP_PATH = path.abspath(path.join(path.join(path.dirname(__file__), '..'), '..'))
flask_app.config['APP_PATH'] = APP_PATH
