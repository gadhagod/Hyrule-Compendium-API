# TODO: region type hints 
from abc import ABC, abstractstaticmethod
from ..constants import Game, db
from .exceptions import RegionNotFound, RegionsNotImplemented
from rockset import F, Q

class Regions(ABC):
    @abstractstaticmethod
    def region_query(
        game: Game,
        where=None
    ):
        return (db.sql(
            Q(f'{game.name}-api-v3.regions')
                .where(where)
                .select(
                    'name', 
                    'shrines', 
                    'dlc_shrines', 
                    'settlements' 
                )
                .limit(1)
        ) if where else db.sql(
            Q(f'{game.name}-api-v3.regions')
                .select(
                    'name', 
                    'shrines', 
                    'dlc_shrines', 
                    'settlements' 
                ))
        ).results()
        
    @abstractstaticmethod
    def get_region(region_name): ...
    
    @abstractstaticmethod
    def get_all(): ...

class BotwRegions(Regions):
    @staticmethod
    def get_region(region_name):
        data = Regions.region_query(
            Game.botw,
            F['name'] == region_name.lower()
        )
        if(data):
            return data[0]
        raise RegionNotFound(region_name, Game.botw)

    @staticmethod
    def get_all():
        return Regions.region_query(Game.botw)

class TotkRegions(Regions):
    @staticmethod
    def get_region(region_name):
        raise RegionsNotImplemented()
        

    @staticmethod
    def get_all():
        raise RegionsNotImplemented()