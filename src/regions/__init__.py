from flask import Flask
from . import views

def loadViews(app: Flask):
    app.add_url_rule('/api/v3/region/<region_name>', view_func=views.get_region)
    app.add_url_rule('/api/v3/regions/<region_name>', view_func=views.get_region)
    app.add_url_rule('/api/v3/regions', view_func=views.get_all)
    app.add_url_rule('/api/v3/regions/all', view_func=views.get_all)
    app.add_url_rule('/api/v3/region/all', view_func=views.get_all)