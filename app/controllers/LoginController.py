from flask import request
from flask_classful import FlaskView
from oort.controllers.BaseController import BaseController

class LoginController(BaseController):
    route_base = "/login"

    def __init__(self) -> None:
        super().__init__()

    def post(self):
        pass
