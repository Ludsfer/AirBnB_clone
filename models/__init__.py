#!/usr/bin/python3
""" This initializes the `models` package """
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
