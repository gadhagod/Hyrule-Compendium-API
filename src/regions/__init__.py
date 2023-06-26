from flask import Blueprint
from . import views

blueprint = Blueprint("regions", __name__)
blueprint.add_url_rule('/<region_name>', view_func=views.region)
blueprint.add_url_rule('/', view_func=views.all)
blueprint.add_url_rule('/all', view_func=views.all)
