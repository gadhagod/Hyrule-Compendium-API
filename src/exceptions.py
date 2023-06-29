from abc import ABC
from werkzeug.exceptions import BadRequest

class ApiException(ABC, Exception): pass

class IllegalGame(BadRequest, ApiException):
    def __init__(self, game: str):
        super().__init__()
        IllegalGame.description = f'game must be "1", "botw", "2", "totk", or not set. "{game}" is invalid'