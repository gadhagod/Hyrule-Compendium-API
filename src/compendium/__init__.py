from flask import Flask
from . import views

def loadViews(app: Flask):
    app.add_url_rule('/api/v3/compendium', view_func=views.all)
    app.add_url_rule('/api/v3/compendium/all', view_func=views.all)
    app.add_url_rule('/api/v3/compendium/master_mode', view_func=views.all_master_mode)
    app.add_url_rule('/api/v3/compendium/master_mode/all', view_func=views.all_master_mode)

    app.add_url_rule('/api/v3/compendium/entry/<inp>', view_func=views.entry)
    app.add_url_rule('/api/v3/compendium/entry/<inp>/image', view_func=views.entry_image)
    app.add_url_rule('/api/v3/compendium/master_mode/entry/<inp>', view_func=views.master_mode_entry)
    app.add_url_rule('/api/v3/compendium/master_mode/entry/<inp>/image', view_func=views.master_mode_entry_image)

    app.add_url_rule('/api/v3/compendium/category/treasure', view_func=views.treasure)
    app.add_url_rule('/api/v3/compendium/category/monsters', view_func=views.monsters)
    app.add_url_rule('/api/v3/compendium/category/materials', view_func=views.materials)
    app.add_url_rule('/api/v3/compendium/category/equipment', view_func=views.equipment)
    app.add_url_rule('/api/v3/compendium/category/creatures', view_func=views.creatures)