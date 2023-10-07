from flask import Flask
from controllers import controller_classes

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello, World!"

for controller_class in controller_classes:    
    controller_class.register(app)

