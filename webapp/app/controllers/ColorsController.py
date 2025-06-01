from flask import request, render_template
from flask_classful import FlaskView
from oort.controllers.BasePageController import BasePageController

class ColorsController(BasePageController):
    route_base = "/colors/"
    
    def __init__(self) -> None:
        super().__init__()

    def index(self):
        meta = self._get_page_meta(title="Oort Framework Color System", description="A Flask-based, object oriented meta-framework.")
        return render_template('colors.jinja', meta=meta, copyright_statement="YYYY Your Name")
