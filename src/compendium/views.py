from typing import Any, Callable, Union, Literal, Dict
from .types import EntryImage
from ..constants import Game, wrap_res
from .main import BotwCompendium, TotkCompendium
from flask import request

def treasure(**kwargs): 
    return wrap_res(
        BotwCompendium.get_category,
        TotkCompendium.get_category,
        **kwargs,
        category="treasure"
    )

def monsters(**kwargs):
    return wrap_res(
        BotwCompendium.get_category,
        TotkCompendium.get_category,
        **kwargs,
        category="monsters"
    )

def materials(**kwargs):
    return wrap_res(
        BotwCompendium.get_category,
        TotkCompendium.get_category,
        **kwargs,
        category="materials"
    )

def equipment(**kwargs):
    return wrap_res(
        BotwCompendium.get_category,
        TotkCompendium.get_category,
        **kwargs,
        category="equipment"
    )

def creatures(**kwargs):
    return wrap_res(
        BotwCompendium.get_category,
        TotkCompendium.get_category,
        **kwargs,
        category="creatures"
    )

def entry(**kwargs):
    return wrap_res(
        BotwCompendium.get_entry,
        TotkCompendium.get_entry,
        **kwargs
    )

def entry_image(**kwargs):
    return wrap_res(
        BotwCompendium.get_entry_image,
        TotkCompendium.get_entry_image,
        is_json=False,
        **kwargs
    )

def all(*args): 
    return wrap_res(
        BotwCompendium.get_all,
        TotkCompendium.get_all
    )

def master_mode_entry(**kwargs): 
    return wrap_res(
        BotwCompendium.get_master_mode_entry,
        TotkCompendium.get_master_mode_entry, 
        **kwargs
    )

def master_mode_entry_image(**kwargs):
    return wrap_res(
        BotwCompendium.get_entry_image,
        TotkCompendium.get_entry_image,
        is_json=False,
        **kwargs,
        master_mode=True
    )

def all_master_mode(**kwargs):
    return wrap_res(
        BotwCompendium.get_all_master_mode_entries,
        TotkCompendium.get_all_master_mode_entries
    )