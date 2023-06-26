from ..constants import Game, IllegalGame, wrap_res
from .main import BotwRegions, TotkRegions

def region(**kwargs): 
    return wrap_res(
        BotwRegions.get_region,
        TotkRegions.get_region,
        **kwargs
    )

def all(**kwargs):
    return wrap_res(
        BotwRegions.get_all,
        TotkRegions.get_all,
        **kwargs
    )