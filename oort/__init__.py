"""End users should not modify the contents of this directory. `oort` provides framework libraries. `app` is the user-land directory. Python files specific to your application belong there."""

from base64 import b64encode
from datetime import datetime
import uuid

def dictify (obj: object, allowed_field_list: list = [], allow_private = False) -> dict:
    """Converts an object's public properties to a dictionary.
    
    Private fields beginning with a single underscore ('_') are excluded unless `allow_private` is set to True. Members beginning with a double underscore ('__') will never be included in the returned dictionary for sanity's sake.

    Binary fields are base64 encoded.

    Parameters:
        allowed_field_list: The allowed_field_list parameter provides a list of acceptable fields. If provided, only fields in the list will be included.
        allow_private: Fields with names that begin with an underscore are treated as private and are not added to the dictionary unless they are specified in the allowed_field_list and allow_private is set to true.

    Return:
        dict
    """
    result_dict = {}

    # We assume that objects follow Python convention and that anything beginning with and
    # underscore is private or is part of Python's internals (e.g. __foo__ like members.)
    # This behavior can be explicitly overridden through the allowed list.
    keys = [name for name in dir(obj) if (not name.startswith('__') and name in allowed_field_list and (allow_private or not name.startswith('_')))]
    use_allowed_list = False
    if len(allowed_field_list) > 0:
        use_allowed_list = True

    for key in keys:
        if not use_allowed_list or key in allowed_field_list:
            value = getattr(obj, key)

            if value == None:
                result_dict[key] = None
            elif not (type(value) is str or type(value) is int or type(value) is float or type(value) is bool):
                # Binary fields are base64 encoded since they can't otherwise be transported in JSON.
                if type(value) is bytes:
                    result_dict[key] = b64encode(value)
                elif type(value) is datetime:
                    result_dict[key] = value.strftime("%m-%d-%Y, %H:%M:%S")
            else:
                result_dict[key] = value



                    
    return result_dict


def dictify_object_list(source_list: list, allowed_field_list: list = [], allow_private = False):
    """Convert a list of object into a list of dictionaries using the objects' public properties.

    Parameters:
        allowed_field_list: The allowed_field_list parameter provides a list of acceptable fields. If provided, only fields in the list will be included.
        allow_private: Fields with names that begin with an underscore are treated as private and are not added to the dictionary unless they are specified in the allowed_field_list and allow_private is set to true.

    Return:
        list
    """
    return_list = []
    for obj in source_list:
        return_list.append(dictify(obj, allowed_field_list, allow_private=allow_private))

    return return_list


def force_to_int (num) -> int:
    """Ensures that user provided integer string are safely converted to integers, even when decimal values are provided. This is useful when verifying that an expected integer-like value (such as a string representation) is in fact integer-like.
    
    Parameters:
        num: A number or a string representation of a number.

    Returns:
        int  Removes any fractional part of a number like value. Will throw an error if provided with a non convertable string or data type.
    """
    return int(round(float(num)))


def is_inty(num) -> int:
    """Returns True if num is integer-like. 4, -4, "4", and "4.0" are all considered to be "inty".

    Parameters:
        num: A number or a string representation of a number.

    Returns:
        bool
    """
    try:
        result = False
        if num == force_to_int(num):
            result = True
        return result
    except:
        return False

import uuid


def is_valid_uuid(value: str, version: int = 1) -> bool:
    try:
        uuid.UUID(str(value), version=version)
        return True
    except ValueError:
        return False


