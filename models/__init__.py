#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
