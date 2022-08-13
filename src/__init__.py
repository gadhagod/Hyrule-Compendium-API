from flask import Blueprint
from .compendium import blueprint as compendium_blueprint
from .regions import blueprint as regions_blueprint

blueprint = Blueprint("blueprint", __name__)
blueprint.register_blueprint(compendium_blueprint, url_prefix="/compendium")
blueprint.register_blueprint(regions_blueprint, url_prefix="/regions")