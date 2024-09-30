from flask import Blueprint
from .exceptions import ApiException
from .compendium import blueprint as compendium_blueprint
from .regions import blueprint as regions_blueprint

blueprint = Blueprint("blueprint", __name__)
blueprint.register_blueprint(compendium_blueprint, url_prefix="/compendium")
blueprint.register_blueprint(regions_blueprint, url_prefix="/regions")

blueprint.register_error_handler(
    ApiException, 
    lambda e: ({'data': {}, 'status': e.code, 'message': e.description}, e.status)
)