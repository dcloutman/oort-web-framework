from typing import List, Optional
from abc import ABC
from urllib import response
from flask import current_app # Necessary for core functionality, such as self.app.logger
from flask import request
from flask_classful import FlaskView
from dotenv import load_dotenv
from os import getenv


class BaseController (FlaskView, ABC):
    """A base view class that applies the most abstract configurations to the controller.

    `route_base` defaults to None, but can be configured via the `OORT_APP_ROUTE_BASE` environment variable to create a prefix for the entire app.
    """

    route_base: str|None = getenv('OORT_APP_ROUTE_BASE', None)
    """
    Sets an application-wide URL prefix. Do not to override this within subclasses.
    Use the `OORT_APP_ROUTE_BASE` environment variable to set this value instead.
    """

    @staticmethod
    def get_base_class():
        """
        This is a critical security feature. Every public method, by default, is converted by Flask Classful to a route,
        including inherited methods. In Oort, the results of get_base_class()) is passed to the Flask app
        and overrides this behavior. The class returned by get_base_class(), and every class it inherits from,
        will not have its public members turned into routes. You can override this method in inheriting
        classes to protect helper methods that you might create within your controllers' inheritence structure.
        """
        return BaseController
    

    def __init__(self) -> None:
        super().__init__()


        self.app = current_app
        """ The same result as calling flask.current_app. Like flask.current_app, self.app can only be used in the context of a request.b
        
        For convinience only. """

        self.request = request
        """ The same result as calling flask.request.
        
        For convinience only. """





