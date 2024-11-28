from typing import Iterable
from abc import ABC, abstractmethod
from pymongo import MongoClient
from os import getenv, path
from enum import StrEnum, EnumMeta
from pymongo.database import Database

from .exceptions import CategoryNonexistant, EntryNonexistant, RegionNonexistant, TotkRegionsNotImplemented, TotkMasterModeNonexistant
from .util import Image

DB_NAME = 'HCI'
DB_URI = f'mongodb+srv://{getenv("MONGO_USERNAME")}:{getenv("MONGO_PASSWORD")}@cluster0.sbbmxpu.mongodb.net'
IMAGE_PATH = path.join(
    path.dirname(path.dirname(path.abspath(__file__))), 
    'images'
)  # gets __file__/../../images

class MetaEnum(EnumMeta): 
    def __contains__(cls, value) -> bool:
        return value in cls._value2member_map_

class PngMachine():
    def __init__(self, image_dir_path):
        self.image_dir_path = image_dir_path
        
    def get_image(self, name):
        file = path.join(self.image_dir_path, f'{name.replace(" ", "_")}.png')
        if path.isfile(file):
            return Image(file)
        
    def get_image_from_subdir(self, subdir, name):
        file = path.join(
            self.image_dir_path, 
            subdir,
            f'{name.replace(" ", "_")}.png'    
        )
        if path.isfile(file):
            return Image(file)

class QueryMachine():
    ''' Wrapper for pymongo that facilitates search across multiple collections '''
    
    def __init__(self, db: Database, collections: Iterable, search_ignore = []):
        self.db = db
        self.collections = collections
        self.search_ignore = search_ignore

    def get_doc(self, collection_name, filter):
        collection = self.db[collection_name]
        return collection.find_one(filter, {'_id': False})
    
    def get_docs(self, collection_name, filter):
        collection = self.db[collection_name]
        return collection.find(filter, {'_id': False})
    
    def search_doc(self, filter):
        for collection in self.collections:
            if collection not in self.search_ignore:
                doc = self.get_doc(collection, filter)
                if doc is not None:
                    return doc
                
    def get_all_docs(self):
        docs = []
        for collection in self.collections:
            if collection not in self.search_ignore:
                docs += self.db[collection].find({}, {'_id': False})
        return docs
    

class RegionFinder(ABC):
    def __init__(self, query_machine: QueryMachine):
        self.query_machine = query_machine
        
    def get_region_with_name(self, name: str):
        region = self.query_machine.search_doc({'name': name})
        if region is None:
            raise RegionNonexistant(name)
        return region

    def get_all_regions(self):
        return self.query_machine.get_all_docs()
    
    
class BotwRegionFinder(RegionFinder):
    def __init__(self, db: Database):
        super().__init__(QueryMachine(db, ['regions-BOTW']))
        
class TotkRegionFinder(RegionFinder):
    def get_region_with_name(self, name: str):
        raise TotkRegionsNotImplemented()
    
    def get_all_regions():
        raise TotkRegionsNotImplemented()


class EntryFinder(ABC):
    def __init__(self, query_machine: QueryMachine):
        self.query_machine = query_machine
                
    def get_entry_with_id(self, id):
        entry = self.query_machine.search_doc({'id': id})
        if entry is None:
            raise EntryNonexistant(id) 
        return entry
    
    def get_entry_with_name(self, name):
        entry = self.query_machine.search_doc({'name': name.replace('_', ' ')})
        if entry is None:
            raise EntryNonexistant(name) 
        return entry
    
    def get_entry(self, id_or_name: str):
        if id_or_name.isnumeric():
            return self.get_entry_with_id(int(id_or_name))
        return self.get_entry_with_name(name=id_or_name)
    
    @abstractmethod
    def get_category(self, collection, category):
        if collection not in self.query_machine.collections or (collection in self.query_machine.search_ignore):
            raise CategoryNonexistant(category)
        return self.query_machine.get_docs(collection, {})
    
    def get_all_entries(self):
        return self.query_machine.get_all_docs()
        
    @abstractmethod
    def get_master_mode_entry(self, id_or_name: str): pass
    
    @abstractmethod
    def get_master_mode_entries(self): pass
    
class TotkEntryFinder(EntryFinder):
    class TotkCategories(StrEnum, metaclass=MetaEnum):
        CREATURES = 'creatures-TOTK'
        EQUIPMENT = 'equipment-TOTK'
        MATERIALS = 'materials-TOTK'
        MONSTERS = 'monsters-TOTK'
        TREASURE = 'treasure-TOTK'
    
    def __init__(self, db: Database):
        super().__init__(QueryMachine(db, self.TotkCategories))
        
    def get_category(self, category):
        return super().get_category(f'{category}-TOTK', category)
        
    def get_master_mode_entry(self, id_or_name: str): 
        raise TotkMasterModeNonexistant()
    
    def get_master_mode_entries(self, id_or_name: str): 
        raise TotkMasterModeNonexistant()

class BotwEntryFinder(EntryFinder):
    class BotwCategories(StrEnum, metaclass=MetaEnum):
        CREATURES = 'creatures-BOTW'
        EQUIPMENT = 'equipment-BOTW'
        MATERIALS = 'materials-BOTW'
        MONSTERS = 'monsters-BOTW'
        TREASURE = 'treasure-BOTW'
        MASTER_MODE = 'master_mode-BOTW'
    
    def __init__(self, db: Database):
        super().__init__(QueryMachine(db, self.BotwCategories, [self.BotwCategories.MASTER_MODE]))
        
    def get_category(self, category):
        return super().get_category(f'{category}-BOTW', category)
        
    def get_master_mode_entry_with_id(self, id: int):
        return self.query_machine.get_doc(self.BotwCategories.MASTER_MODE, {'id': id})

    def get_master_mode_entry_with_name(self, name: str):
        return self.query_machine.get_doc(self.BotwCategories.MASTER_MODE, {'name': name})
    
    def get_master_mode_entry(self, id_or_name: str):
        if id_or_name.isnumeric():
            return self.get_master_mode_entry_with_id(int(id_or_name))
        return self.get_master_mode_entry_with_name(id_or_name)
    
    def get_master_mode_entries(self):
        return self.query_machine.get_docs(self.BotwCategories.MASTER_MODE, {})
        
        
class ImageFinder(ABC):
    def __init__(self, entry_finder: EntryFinder, image_dir_path):
        self.entry_finder = entry_finder
        self.png_machine = PngMachine(image_dir_path)
        
    def get_image_with_name(self, name: str):
        image = self.png_machine.get_image(name)
        if image is None:
            raise EntryNonexistant(name)
        return image
        
    def get_image_with_id(self, id: int):
        entry = self.entry_finder.get_entry_with_id(id)
        return self.get_image_with_name(entry['name'])
    
    def get_image(self, id_or_name: str):
        if id_or_name.isnumeric():
            return self.get_image_with_id(int(id_or_name))
        return self.get_image_with_name(id_or_name)
    
    @abstractmethod
    def get_master_mode_image(id_or_name: str): pass
        
class BotwImageFinder(ImageFinder):
    def __init__(self, entry_finder: BotwEntryFinder):
        super().__init__(entry_finder, path.join(IMAGE_PATH, 'BOTW'))
        
    def get_master_mode_image_with_name(self, name: str):
        image = self.png_machine.get_image_from_subdir('master_mode', name)    
        if image is None:
            raise EntryNonexistant(name)
        return image
        
    def get_master_mode_image_with_id(self, id: int):
        entry = self.entry_finder.get_master_mode_entry_with_id(id)
        return self.get_master_mode_image_with_name(entry['name'])
    
    def get_master_mode_image(self, id_or_name: str):
        if id_or_name.isnumeric():
            return self.get_master_mode_image_with_id(int(id_or_name))
        return self.get_master_mode_image_with_name(id_or_name)

class TotkImageFinder(ImageFinder):
    def __init__(self, entry_finder: TotkEntryFinder):
        super().__init__(entry_finder, path.join(IMAGE_PATH, 'TOTK'))
        
    def get_master_mode_image(self, id_or_name: str):
        raise EntryNonexistant(id_or_name)


db = MongoClient(DB_URI)[DB_NAME]  # this creates a new db object every time this file is imported
                                   # TODO: make this constant/global