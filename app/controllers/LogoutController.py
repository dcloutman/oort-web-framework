from flask import request
from flask_classful import FlaskView
from oort.controllers.BaseDataController import BaseController

class LogoutController(BaseController):
    route_base = "/logout"

    def __init__(self) -> None:
        print(self.get_base_class())
        super().__init__()

    def post(self):
        pass
