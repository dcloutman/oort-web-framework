from oort.controllers.BaseController import BaseController

class BasePageController (BaseController):
    """Extend this controller to build basic page end-points.
    """
    def __init__(self) -> None:
        super().__init__()


    def _get_page_meta (self, title="", description="", keywords=""):
        return {
            "title": title,
            "description": description,
            "keywords": keywords
        }
