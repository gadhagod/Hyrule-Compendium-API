from flask import Blueprint

from .util import wrap_res
from .db import BotwRegionFinder, TotkRegionFinder, db

botw_regions = BotwRegionFinder(db)
totk_regions = TotkRegionFinder(db)

def region(**kwargs):
    return wrap_res(
        botw_regions.get_region_with_name,
        totk_regions.get_region_with_name,
        **kwargs
    )

def all_regions(**kwargs):
    return wrap_res(
        botw_regions.get_all_regions,
        totk_regions.get_all_regions,
        **kwargs
    )

blueprint = Blueprint('regions', __name__)

blueprint.add_url_rule('/<name>', view_func=region)
blueprint.add_url_rule('/', view_func=all_regions)
blueprint.add_url_rule('/all', view_func=all_regions)
