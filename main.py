"""
*Warning:* This file belongs to the Oort meta-framework and should not be modified by
 application developers. The contents of this file are subject to change with framework updates.
"""

from flask import Flask
from app.controllers import controller_classes
app = Flask(__name__)
app.config.from_object('app.config')

@app.route("/hello")
def hello_world():
    return "Hello, World!"

for controller_class in controller_classes:    
    controller_class.register(app)

