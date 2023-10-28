from flask import request
from flask_classful import FlaskView
from oort.controllers.BaseController import BaseController

class IndexController(BaseController):
    route_base = "/"
    
    def __init__(self) -> None:
        super().__init__()

    def index(self):
        return  "Index page!"