import flask
from flask_cors import CORS

def get_response(*args, **kwargs):
    return {
        'data': {}, 
        'status': 410, 
        'message': 'HCA v1 and v2 have been discontinued. Please see the migraiton guide at https://github.com/gadhagod/Hyrule-Compendium-API/issues/46'
    }, 410

v2_blueprint = flask.Blueprint('v2_blueprint', __name__)

v2_blueprint.add_url_rule('/api/v1', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/all', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/all', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/master_mode', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/master_mode', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/master_mode/all', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/master_mode/all', view_func=get_response)

v2_blueprint.add_url_rule('/api/v1/entry/<inp>', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/entry/<inp>', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/entry/<inp>/image', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/entry/<inp>/image', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/master_mode/entry/<inp>', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/master_mode/entry/<inp>', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/master_mode/entry/<inp>/image', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/master_mode/entry/<inp>/image', view_func=get_response)

v2_blueprint.add_url_rule('/api/v1/category/treasure', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/category/treasure', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/category/monsters', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/category/monsters', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/category/materials', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/category/materials', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/category/equipment', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/category/equipment', view_func=get_response)
v2_blueprint.add_url_rule('/api/v1/category/creatures', view_func=get_response)
v2_blueprint.add_url_rule('/api/v2/category/creatures', view_func=get_response)

if __name__ == '__main__':  
    app = flask.Flask(__name__)
    CORS(app)
    app.register_error_handler(500, lambda ctx: ({'data': {}, 'message': 'Server error'}, 500))
    app.register_error_handler(404, lambda ctx: ({'data': {}, 'message': 'Not found'}, 404))
    app.register_blueprint(v2_blueprint)
    app.run(debug=True)