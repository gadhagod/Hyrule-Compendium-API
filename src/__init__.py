from flask import Flask
from . import compendium, regions

def loadViews(app: Flask):
    compendium.loadViews(app)
    regions.loadViews(app)