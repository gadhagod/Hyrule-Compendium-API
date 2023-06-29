from rockset import F, Q
from abc import ABC, abstractstaticmethod
from typing import Union
from flask import send_from_directory
from .exceptions import EntryNotFound, IllegalMasterModeEntryName, TotkImagesNotImplemented
from ..constants import Game, db
from .types import (
    EntrySelects, 
    EntrySelectsOptions, 
    Where, 
    StandardCategoryName, 
    EntryImage,
    DlcCategoryName,
    Optional,
    BaseEntrySelect,
    EntryData,
    EntrySelectsOptions,
    CategoryData
)

class Compendium(ABC):
    _selects: EntrySelectsOptions
    
    @staticmethod
    def _query(
        game: Game,
        category: Union[StandardCategoryName, DlcCategoryName],
        where: Optional[bool]=None,
        select: list[BaseEntrySelect]=[],
        limit: Optional[int]=None
    ) -> list[EntryData]: 
        query = Q(f'{game.name}-api-v3.{category}')
        if where:
            query = query.where(where)
        query = query.select(
            'id', 
            'name', 
            'description', 
            'common_locations', 
            'image', 
            'category',
            'dlc', 
            *map(lambda i: F[i], select)
        )
        return db.sql(
            query.limit(limit) if limit else query
        ).results()
    
    @abstractstaticmethod    
    def _get_selects(category: str) -> EntrySelectsOptions: ...

    @abstractstaticmethod    
    def get_category(category: str) -> CategoryData: ...
    
    @abstractstaticmethod    
    def get_entry(where: Where)-> tuple[StandardCategoryName, EntryData]: ...

    @abstractstaticmethod    
    def get_entry_image(inp: str, master_mode: bool) -> EntryImage: ...

    @abstractstaticmethod
    def get_all() -> list[EntryData]: ...
    
    @abstractstaticmethod
    def get_master_mode_entry(inp: str) -> EntryData: ...
    
    @abstractstaticmethod
    def get_all_master_mode_entries() -> list[EntryData]: ...
    
    
class BotwCompendium(Compendium):
    _selects = {
        'treasure': {'drops'},
        'monsters': {'drops'},
        'materials': {'cooking_effect', 'hearts_recovered'},
        'equipment': {'properties'},
        'creatures': {
            'edible': {'hearts_recovered', 'cooking_effect', 'edible'},
            'inedible': {'drops', 'edible'}
        }
    }
    
    def _get_selects(category: StandardCategoryName) -> EntrySelects:
        return BotwCompendium._selects[category]
    
    @staticmethod
    def get_category(category: StandardCategoryName) -> CategoryData:
        category = category.lower()
        if category == 'creatures':
            return (
                Compendium._query(
                    Game.botw,
                    category='creatures', 
                    where=F['edible'] == True, 
                    select=BotwCompendium._selects['creatures']['edible']
                )
                + 
                Compendium._query(
                    Game.botw,
                    category='creatures', 
                    where=F['edible'] == False, 
                    select=BotwCompendium._selects['creatures']['inedible']
                )
            )
        return Compendium._query(Game.botw, category=category, select=BotwCompendium._selects[category])

    def get_entry(inp: str) -> EntryData:
        where = (F['id'] == int(inp)) if inp.isnumeric() else F['name'] == inp.lower().replace('_', ' ')
        for category in list(BotwCompendium._selects.keys())[:-1]:
            res = Compendium._query(
                Game.botw,
                category=category, 
                where=where, 
                select=BotwCompendium._selects[category]
            )
            if res:
                return res[0]

        res = Compendium._query(
            Game.botw,
            category='creatures',
            where=where,
            select=BotwCompendium._selects['creatures']['edible'].union(BotwCompendium._selects['creatures']['inedible']),
            limit=1
        )

        if res:
            if res[0]['edible']:
                for select in BotwCompendium._selects['creatures']['inedible']:
                    if select not in BotwCompendium._selects['creatures']['edible']:
                        res[0].pop(select, None)
            else:
                for select in BotwCompendium._selects['creatures']['edible']:
                    if select not in BotwCompendium._selects['creatures']['inedible']:
                        res[0].pop(select, None)
            return res[0]
        else:
            raise EntryNotFound(inp, Game.botw)

    @staticmethod
    def get_entry_image(inp, master_mode=False) -> EntryImage:
        if inp == 'master_mode':
            raise IllegalMasterModeEntryName()

        target_entry = None
        if master_mode:
            if inp.isnumeric():
                res = Compendium._query(
                    Game.botw,
                    category='master_mode',
                    where=(F['_id'] == inp),
                )
                if res:
                    target_entry = res[0]['name']
            else:
                target_entry = inp
        else:
            if inp.isnumeric():
                for category in BotwCompendium._selects.keys():
                    res = Compendium._query(
                        Game.botw,
                        category=category,
                        where=(F['_id'] == inp),
                    )
                    if res:
                        target_entry = res[0]['name']
                        break
            else:
                target_entry = inp

        if not target_entry:
            raise EntryNotFound(inp, Game.botw)

        try:
            return send_from_directory(
                f'db/botw/data/compendium/images{"/master_mode" if master_mode else ""}', 
                f"{target_entry.replace(' ', '_').replace('+', '＋')}.png", 
                mimetype='image/png'
            )
        except FileNotFoundError:
            raise EntryNotFound(inp, Game.botw)

    @staticmethod
    def get_all() -> list[EntryData]:
        all_data = []
        for category in BotwCompendium._selects.keys():
            all_data.extend(BotwCompendium.get_category(category))
        return all_data

    @staticmethod
    def get_master_mode_entry(inp) -> EntryData:
        name, id = ('', int(inp)) if inp.isnumeric() else (inp.replace('_', ' '), 0)
        res = Compendium._query(
            game=Game.botw,
            category='master_mode',
            where=(F['name'] == name) | (F['id'] == id),
            select=BotwCompendium._selects['monsters'],
            limit=1
        )
        if res:
            return res[0]
        else:
            raise EntryNotFound(inp, Game.botw)

    @staticmethod
    def get_all_master_mode_entries() -> list[EntryData]:
        return Compendium._query(
            game=Game.botw,
            category='master_mode',
            select=BotwCompendium._selects['monsters']
        )
        
        
class TotkCompendium(Compendium):
    _selects = {
        'treasure': {'drops'},
        'monsters': {'drops'},
        'materials': {'cooking_effect', 'hearts_recovered', 'fuse_attack_power'},
        'equipment': {'properties'},
        'creatures': {
            'edible': {'hearts_recovered', 'cooking_effect', 'edible'},
            'inedible': {'drops', 'edible'}
        }
    }
    
    def _get_selects(category: StandardCategoryName) -> EntrySelects:
        return TotkCompendium._selects[category]
    
    @staticmethod
    def get_category(category: StandardCategoryName) -> CategoryData:
        category = category.lower()
        if category == 'creatures':
            return Compendium._query(
                    Game.totk,
                    category='creatures', 
                    where=F['edible'] == True, 
                    select=TotkCompendium._selects['creatures']['edible']
                ) + Compendium._query(
                    Game.totk,
                    category='creatures', 
                    where=F['edible'] == False, 
                    select=TotkCompendium._selects['creatures']['inedible']
                )
            
        return Compendium._query(
            Game.totk,
            category=category, 
            select=TotkCompendium._selects[category]
        )

    def get_entry(inp: str) -> EntryData:
        where = (F['id'] == int(inp)) if inp.isnumeric() else F['name'] == inp.lower().replace('_', ' ')
        for category in list(TotkCompendium._selects.keys())[:-1]:
            res = Compendium._query(
                Game.totk,
                category=category, 
                where=where, 
                select=TotkCompendium._selects[category]
            )
            if res:
                return res[0]

        res = Compendium._query(
            Game.totk,
            category='creatures',
            where=where,
            select=TotkCompendium._selects['creatures']['edible'].union(TotkCompendium._selects['creatures']['inedible'])
        )

        if res:
            if res[0]['edible']:
                for select in TotkCompendium._selects['creatures']['inedible']:
                    if select not in TotkCompendium._selects['creatures']['edible']:
                        res[0].pop(select, None)
            else:
                for select in TotkCompendium._selects['creatures']['edible']:
                    if select not in TotkCompendium._selects['creatures']['inedible']:
                        res[0].pop(select, None)
            return res[0]
        else:
            raise EntryNotFound(inp, Game.totk)

    @staticmethod
    def get_entry_image(inp: int, master_mode=False) -> EntryImage:
        raise TotkImagesNotImplemented()

    @staticmethod
    def get_all() -> list[EntryData]:
        all_data = []
        for category in TotkCompendium._selects.keys():
            all_data.extend(TotkCompendium.get_category(category))
        return all_data

    @staticmethod
    def get_master_mode_entry(inp) -> EntryData:
        name, id = ('', int(inp)) if inp.isnumeric() else (inp.replace('_', ' '), 0)
        res = Compendium._query(
            Game.totk,
            category='master_mode',
            where=(F['name'] == name) | (F['id'] == id),
            select=TotkCompendium._selects['monsters'],
            limit=1
        )
        if res:
            return res[0]
        else:
            raise EntryNotFound(inp, Game.totk)

    @staticmethod
    def get_all_master_mode_entries() -> list[EntryData]:
        return Compendium._query(
            Game.totk,
            category='master_mode',
            select=TotkCompendium._selects['monsters']
        )