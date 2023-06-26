from .exceptions import IllegalGame
from abc import ABC
from typing import Final, Callable
from rockset import Client
from os import getenv
from enum import Enum
from flask import request

Game: Final =  Enum('Game', ['botw', 'totk'])
db: Final = Client(api_key=getenv('RS2_TOKEN'), api_server='api.rs2.usw2.rockset.com')
      
def get_game() -> Game:
    game = request.args.get('game')
    if not game or game == '1' or game == 'botw':
        return Game.botw
    elif game == '2' or game == 'totk':
        return Game.totk
    else:
        raise IllegalGame(game)
        
def wrap_res(
    botw_method: Callable, 
    totk_method: Callable, 
    is_json=True, 
    **kwargs
):  
    method = (botw_method if get_game() == Game.botw else totk_method)
    response = method(**kwargs)
    if is_json:
        return {'data': response}
    else:
        return response