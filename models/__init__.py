#!/usr/bin/python3
"""Making models directory a package."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
