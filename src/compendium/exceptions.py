from typing import Union
from ..constants import Game
from ..exceptions import ApiException
from werkzeug.exceptions import BadRequest, NotFound, NotImplemented

class EntryNotFound(NotFound, ApiException):
    def __init__(self, entry: Union[int, str], game: Game):
        super().__init__()
        EntryNotFound.description = f'Entry with name or ID "{entry}" does not exist in the specified game, {game.name}'

class IllegalMasterModeEntryName(BadRequest, ApiException):
    def __init__(self):
        super().__init__()
        IllegalMasterModeEntryName.description = '"master_mode" is not a valid entry name. If you want to access a master mode entry, you must use /compendium/master_mode/<entry>'
    
class TotkImagesNotImplemented(NotImplemented, ApiException):
    def __init__(self) -> None:
        super().__init__()
        TotkImagesNotImplemented.description = 'Totk regions have not been implemented yet'