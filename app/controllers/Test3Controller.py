from flask import request
from flask_classful import FlaskView

class Test3Controller(FlaskView):
    def __init__(self) -> None:
        super().__init__()


        self.app = current_app
        """ The same result as calling flask.current_app.
        
        For convinience only. """
