import flask
from flask_cors import CORS
from src.utils import redirectToDocs
from src import loadViews

app = flask.Flask(__name__, static_folder='compendium/images')
CORS(app)

app.register_error_handler(500, lambda ctx: ({'data': {}, 'message': 'Server error'}, 500))
app.register_error_handler(404, lambda ctx: ({'data': {}, 'message': 'Not found'}, 404))
app.add_url_rule('/', view_func=redirectToDocs)
app.add_url_rule('/api', view_func=redirectToDocs)
app.add_url_rule('/api/v3', view_func=lambda: {})
loadViews(app)

if __name__ == '__main__': # testing server
    app.run(debug=True)
else: # production server
    # precondition: setup_versioning.sh executed
    ""
    from v2.server import v2_blueprint
    app.register_blueprint(v2_blueprint)