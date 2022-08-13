from flask import Blueprint
from . import views

blueprint = Blueprint("compendium", __name__)

blueprint.add_url_rule('/', view_func=views.all)
blueprint.add_url_rule('/all', view_func=views.all)
blueprint.add_url_rule('/master_mode', view_func=views.all_master_mode)
blueprint.add_url_rule('/master_mode/all', view_func=views.all_master_mode)

blueprint.add_url_rule('/entry/<inp>', view_func=views.entry)
blueprint.add_url_rule('/entry/<inp>/image', view_func=views.entry_image)
blueprint.add_url_rule('/master_mode/entry/<inp>', view_func=views.master_mode_entry)
blueprint.add_url_rule('/master_mode/entry/<inp>/image', view_func=views.master_mode_entry_image)

blueprint.add_url_rule('/category/treasure', view_func=views.treasure)
blueprint.add_url_rule('/category/monsters', view_func=views.monsters)
blueprint.add_url_rule('/category/materials', view_func=views.materials)
blueprint.add_url_rule('/category/equipment', view_func=views.equipment)
blueprint.add_url_rule('/category/creatures', view_func=views.creatures)