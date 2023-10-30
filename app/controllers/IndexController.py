from flask import request, render_template
from flask_classful import FlaskView
from oort.controllers.BasePageController import BasePageController

class IndexController(BasePageController):
    route_base = "/"
    
    def __init__(self) -> None:
        super().__init__()

    def index(self):
        page_headline = "Oort Web Framework"
        page_content = """<strong>Oort</strong> is a Flask-based, object oriented meta-framework.
                        """
        meta = self._get_page_meta(title="Oort Web Framework", description="A Flask-based, object oriented meta-framework.")
        return render_template('index.jinja', content_headline=page_headline, content_text=page_content, meta=meta, copyright_statement="2023 David Cloutman.")
