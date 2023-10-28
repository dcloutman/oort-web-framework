"""
*Warning:* This file belongs to the Oort meta-framework and should not be modified by
 application developers. The contents of this file are subject to change with framework updates.
"""

from glob import glob
from inspect import getmembers
from os.path import basename, dirname, isfile, join
from importlib import import_module
from flask import current_app # Necessary for core functionality, such as self.app.logger

__all__ = ['controller_classes']

modules = glob(join(dirname(__file__), "*Controller.py"))
controller_names = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
controller_classes = []
for controller_name in controller_names:
    controller_module = import_module(__name__ + '.' + controller_name)
    controller_class = None
    for member_tuple in getmembers(controller_module):
        if member_tuple[0] == controller_name:
            controller_class = member_tuple[1]
            controller_classes.append(controller_class)
            break
