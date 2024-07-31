from pymongo import MongoClient
from typing import Final, Callable
from sys import argv
from os import getenv
from enum import Enum
from flask import request, send_file
from bson.json_util import dumps
from pymongo.cursor import Cursor

from .exceptions import IllegalGame

class Game(Enum):
    BOTW = 1
    TOTK = 2
      
class Image(str): 
    def send(self):
        return send_file(
            self.__str__(), 
            mimetype='image/png',
            download_name=self.__str__()
        )
      
def get_game() -> Game:
    game = request.args.get('game')
    if not game or game == '1' or game == 'botw':
        return Game.BOTW
    elif game == '2' or game == 'totk':
        return Game.TOTK
    else:
        raise IllegalGame(game)
        
def wrap_res(
    botw_method: Callable, 
    totk_method: Callable,
    **kwargs
):  
    method = (botw_method if get_game() == Game.BOTW else totk_method)
    response = method(**kwargs)
    if isinstance(response, Image):
        return response.send()
    if isinstance(response, Cursor):
        response = list(response)
    return {
        'data': response,
        'status': 500,
        'message': ''
    }