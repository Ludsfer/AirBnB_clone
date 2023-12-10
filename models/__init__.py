#!/usr/bin/python3
""" This initializes a package."""
from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
