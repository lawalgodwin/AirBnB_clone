#!/usr/bin/python3
"""This file creates a storage initializes the storage

   the created storage serves as the single source of truth
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
