from flask import Flask
from . import views

def loadViews(app: Flask):
    app.add_url_rule('/api/v3/region/<category_name>', view_func=views.get_category)
    app.add_url_rule('/api/v3/regions', view_func=views.get_all)
    app.add_url_rule('/api/v3/regions/all', view_func=views.get_all)
    app.add_url_rule('/api/v3/region/all', view_func=views.get_all)