#!/usr/bin/python3
"""
models package 
"""

TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")
if TYPE_STORAGE == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

