import typing as t
from werkzeug.sansio.response import Response
from ..constants import Game
from ..exceptions import ApiException
from werkzeug.exceptions import NotFound, NotImplemented

class RegionNotFound(NotFound, ApiException):
    def __init__(self, region: str, game: Game):
        super().__init__()
        RegionNotFound.description = f'Region with name "{region}" does not exist in the specified game, {game.name}'
        
class RegionsNotImplemented(NotImplemented, ApiException):
    def __init__(self) -> None:
        super().__init__()
        RegionsNotImplemented.description = 'Totk regions have not been implemented yet'