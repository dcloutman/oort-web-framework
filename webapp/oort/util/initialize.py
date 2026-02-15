from tempfile import tempdir
from flask import Flask
from flask_cors import CORS
from os import path, environ, pardir
from pathlib import Path

flask_app = Flask(__name__, static_folder="../../static", template_folder="../../templates")

allowed_origins_string = environ.get('OORT_CORS_ALLOWED_ORIGINS', '')
"""
A comma-separated list of allowed origins for CORS requests.
"""

if not allowed_origins_string == '':
    allowed_origins: list[str] = allowed_origins_string.split(',')
    CORS(flask_app, origins=allowed_origins)

# Set the app path to the root of the application
APP_PATH = path.abspath(path.join(path.join(path.dirname(__file__), '..'), '..'))
flask_app.config['APP_PATH'] = APP_PATH
