from flask import request
from flask_classful import FlaskView
from oort.controllers.BaseController import BaseController

class Test5Controller(BaseController):
    def __init__(self) -> None:
        super().__init__()


        self.app = current_app
        """ The same result as calling flask.current_app.
        
        For convinience only. """
