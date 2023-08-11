#!usr/bin/python3
from models.engine.file_storage import FileStorage
"creates unique filestorage instance for the app"


storage = FileStorage()
storage.reload()
