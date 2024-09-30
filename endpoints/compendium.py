from flask import Blueprint

from .util import wrap_res
from .db import BotwEntryFinder, TotkEntryFinder, BotwImageFinder, TotkImageFinder, db

botw_compendium = BotwEntryFinder(db)
totk_compendium = TotkEntryFinder(db)
botw_image_compendium = BotwImageFinder(botw_compendium)
totk_image_compendium = TotkImageFinder(totk_compendium)

def category(**kwargs):
    return wrap_res(
        botw_compendium.get_category,
        totk_compendium.get_category,
        **kwargs
    )

def entry(**kwargs):
    return wrap_res(
        botw_compendium.get_entry,
        totk_compendium.get_entry,
        **kwargs
    )

def entry_image(**kwargs):
    return wrap_res(
        botw_image_compendium.get_image,
        totk_image_compendium.get_image,
        **kwargs
    )

def category_entries(**kwargs):
    return wrap_res(
        botw_compendium.get_category,
        totk_compendium.get_category,
        **kwargs
    )

def all_entries(**kwargs): 
    return wrap_res(
        botw_compendium.get_all_entries,
        totk_compendium.get_all_entries,
        **kwargs
    )

def master_mode_entry(**kwargs): 
    return wrap_res(
        botw_compendium.get_master_mode_entry,
        totk_compendium.get_master_mode_entry, 
        **kwargs
    )

def master_mode_entry_image(**kwargs):
    return wrap_res(
        botw_image_compendium.get_image,
        totk_image_compendium.get_image,
        **kwargs
    )

def all_master_mode_entries(**kwargs):
    return wrap_res(
        botw_compendium.get_master_mode_entries,
        totk_compendium.get_master_mode_entries,
        **kwargs
    )

blueprint = Blueprint('compendium', __name__)

blueprint.add_url_rule('/', view_func=all_entries)
blueprint.add_url_rule('/all', view_func=all_entries)
blueprint.add_url_rule('/master_mode', view_func=all_master_mode_entries)
blueprint.add_url_rule('/master_mode/all', view_func=all_master_mode_entries)

blueprint.add_url_rule('/entry/<id_or_name>', view_func=entry)
blueprint.add_url_rule('/entry/<id_or_name>/image', view_func=entry_image)
blueprint.add_url_rule('/master_mode/entry/<id_or_name>', view_func=master_mode_entry)
blueprint.add_url_rule('/master_mode/entry/<id_or_name>/image', view_func=master_mode_entry_image )

blueprint.add_url_rule('/category/<category>', view_func=category_entries)