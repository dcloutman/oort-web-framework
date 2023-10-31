from flask import request
from flask_classful import FlaskView
from oort.controllers.BaseController import BaseController
from abc import ABC

class LoginHelperController(BaseController, ABC):
    """
    Safely contains helper methods without exposing them as routes. Autoloader should not register this.
    """

    @staticmethod
    def get_base_class():
        return LoginHelperController

class LoginController(LoginHelperController):
    route_base = "/login"

    def __init__(self) -> None:
        super().__init__()

    def post(self):
        pass
