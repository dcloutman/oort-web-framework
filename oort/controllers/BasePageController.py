from oort.controllers.BaseController import BaseController

class BasePageController (BaseController):
    @staticmethod
    def get_base_class():
        """
        This is a critical security feature. Every public method, by default, is converted by Flask Classful to a route,
        including inherited methods. In Oort, the results of get_base_class()) is passed to the Flask app
        and overrides this behavior. The class returned by get_base_class(), and every class it inherits from,
        will not have its public members turned into routes. You can override this method in inheriting
        classes to protect helper methods that you might create within your controllers' inheritence structure.
        """
        return BasePageController

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
