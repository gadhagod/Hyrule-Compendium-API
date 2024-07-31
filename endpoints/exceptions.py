from abc import ABC
from typing import Union
from werkzeug.exceptions import BadRequest, NotImplemented, NotFound
from werkzeug.sansio.response import Response

class ApiException(ABC, Exception): pass

class IllegalGame(BadRequest, ApiException):
    def __init__(self, game: str):
        super().__init__()
        IllegalGame.description = f'Game must be "1", "botw", "2", "totk", or not set. "{game}" is invalid'

class CategoryNonexistant(NotFound, ApiException):
    def __init__(self, category: str):
        super().__init__()
        CategoryNonexistant.description = f'Category "{category}" does not exist'

class RegionNonexistant(NotFound, ApiException):
    def __init__(self, region: str):
        super().__init__()
        RegionNonexistant.region = f'Region "{region}" does not exist'

class EntryNonexistant(NotFound, ApiException):
    def __init__(self, entry_id_or_name: Union[str, int]):
        super().__init__()
        if type(entry_id_or_name) == int or (type(entry_id_or_name) == str and entry_id_or_name.isnumeric()):
            EntryNonexistant.description = f'Entry with ID {entry_id_or_name} does not exist'
        else:
            EntryNonexistant.description = f'Entry "{entry_id_or_name}" does not exist'
            
class TotkMasterModeNonexistant(NotFound, ApiException):
    def __init__(self, entry_id_or_name: Union[str, int]):
        super().__init__()
        TotkMasterModeNonexistant.description = f'Master mode doesn\'t exist in TOTK'
            
class TotkRegionsNotImplemented(NotImplemented, ApiException):
    def __init__(self) -> None:
        TotkRegionsNotImplemented.description = f'TOTK regions not yet implemented'