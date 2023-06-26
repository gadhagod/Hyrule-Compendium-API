from typing import Union
from ..constants import Game
from ..exceptions import ApiException
from werkzeug.exceptions import BadRequest, NotFound

class EntryNotFound(NotFound, ApiException):
    def __init__(self, entry: Union[int, str], game: Game):
        super().__init__()
        EntryNotFound.description = f'Entry with name or ID "{entry}" does not exist in the specified game, {game.name}'

class IllegalMasterModeEntryName(BadRequest, ApiException):
    description = '"master_mode" is not a valid entry name. If you want to access a master mode entry, you must use /compendium/master_mode/<entry>'