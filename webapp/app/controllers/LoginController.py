from flask import request, flash, redirect, url_for
from flask_login import login_user
from abc import ABC
from oort.lib.auth import AuthUser
from oort.controllers.BaseController import BaseController


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
        http_status = None
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if username != "admin" or password != "dontdothisinproduction":
            http_status = 200
            flash('Bad login', 'error')
        else:
            http_status = 401
            user = AuthUser("admin")
            user.authenticated = True
            login_user(user)
            flash('Logged in successfully.', 'success')

        return redirect('/', code=http_status)
