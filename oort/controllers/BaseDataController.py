from oort.controllers.BaseController import BaseController
from abc import ABC

class BaseDataController(BaseController, ABC):
    def __init__(self) -> None:
        super().__init__()

        self.json = None
        """Stores JSON body from the HTTP request if present. See before() for processing details."""

    def get_writable_fields (self):
        """Dynamically generates a list of fields that are writable by the API.
        
        Removes read only fields from the exposed_field_names and returns the results.
        """
        return list(set(self.exposed_fields) - set(self.read_only_fields))


    def before_request (self, name, *args, **kwargs):
        """
        Automatically process JSON. If overriding this method, be sure to call this parent method or processing of
        JSON requests may break.
        """
        if self.request.is_json:
            self.json = self.request.get_json()


    def _common_name_by_number(self, num: int, capitalize:bool = False, all_caps: bool = False) -> str:
        """Get correct noun form for number using common_name_singular and common_name_plural properties.

        Arguments:
            capitalize: bool  The first letter will be capitalized.
            all_caps: bool  All characters will be capitalized. Causes capitalize = False to be ignored.

        Returns: 
            str: A human readable descriptor for the entities for display in result messages.
        """
        common_name = self.common_name_singular if num == 1 else self.common_name_plural
        if all_caps:
            return common_name.upper()
        if capitalize:
            return common_name.capitalize()
        
        return common_name
