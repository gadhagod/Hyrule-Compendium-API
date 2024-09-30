import flask
from flask_cors import CORS
from endpoints import blueprint, exceptions
from werkzeug.exceptions import NotFound

def redirectToDocs(): return flask.redirect('https://gadhagod.github.io/Hyrule-Compendium-API')

app = flask.Flask(__name__, static_folder='compendium/images')
app.app_context()
CORS(app)
    
app.register_error_handler(
    500,
    lambda e: ({'data': {}, 'status': 500, 'message': 'Server error'}, 500)
)

app.register_error_handler(
    NotFound,   
    lambda e: ({
        'data': {}, 
        'status': 404, 
        'message': e.description if isinstance(e, exceptions.ApiException) 
            else "endpoint does not exist"
    }, 404)
)

app.add_url_rule('/', view_func=redirectToDocs)
app.add_url_rule('/api', view_func=redirectToDocs)
app.add_url_rule('/api/v3', view_func=redirectToDocs)
app.register_blueprint(blueprint, url_prefix='/api/v3')

if __name__ == '__main__': # dev server
    app.run(debug=True)
else: # prod server
    pass