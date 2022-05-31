from src import view_funcs
import flask
from flask_cors import CORS

func_cnt = 0
def load_view(view_func, version, inp=False):
    global func_cnt
    wrapper = (lambda inp : view_func(version, inp)) if inp else lambda : view_func(version)
    wrapper.__name__ = str(func_cnt)
    func_cnt += 1
    return wrapper

v2_blueprint = flask.Blueprint('v2_blueprint', __name__)

v2_blueprint.add_url_rule('/api/v1', view_func=load_view(view_funcs.all, 'v1'))
v2_blueprint.add_url_rule('/api/v2', view_func=load_view(view_funcs.all, 'v2'))
v2_blueprint.add_url_rule('/api/v1/all', view_func=load_view(view_funcs.all, 'v1'))
v2_blueprint.add_url_rule('/api/v2/all', view_func=load_view(view_funcs.all, 'v2'))
v2_blueprint.add_url_rule('/api/v1/master_mode', view_func=load_view(view_funcs.all_master_mode, 'v1'))
v2_blueprint.add_url_rule('/api/v2/master_mode', view_func=load_view(view_funcs.all_master_mode, 'v2'))
v2_blueprint.add_url_rule('/api/v1/master_mode/all', view_func=load_view(view_funcs.all_master_mode, 'v1'))
v2_blueprint.add_url_rule('/api/v2/master_mode/all', view_func=load_view(view_funcs.all_master_mode, 'v2'))

v2_blueprint.add_url_rule('/api/v1/entry/<inp>', view_func=load_view(view_funcs.entry, 'v1', inp=True))
v2_blueprint.add_url_rule('/api/v2/entry/<inp>', view_func=load_view(view_funcs.entry, 'v2', inp=True))
v2_blueprint.add_url_rule('/api/v1/entry/<inp>/image', view_func=load_view(view_funcs.entry_image, 'v1', inp=True))
v2_blueprint.add_url_rule('/api/v2/entry/<inp>/image', view_func=load_view(view_funcs.entry_image, 'v2', inp=True))
v2_blueprint.add_url_rule('/api/v1/master_mode/entry/<inp>', view_func=load_view(view_funcs.master_mode_entry, 'v1', inp=True))
v2_blueprint.add_url_rule('/api/v2/master_mode/entry/<inp>', view_func=load_view(view_funcs.master_mode_entry, 'v2', inp=True))
v2_blueprint.add_url_rule('/api/v1/master_mode/entry/<inp>/image', view_func=load_view(view_funcs.master_mode_entry_image, 'v1', inp=True))
v2_blueprint.add_url_rule('/api/v2/master_mode/entry/<inp>/image', view_func=load_view(view_funcs.master_mode_entry_image, 'v2', inp=True))

v2_blueprint.add_url_rule('/api/v1/category/treasure', view_func=load_view(view_funcs.treasure, 'v1'))
v2_blueprint.add_url_rule('/api/v2/category/treasure', view_func=load_view(view_funcs.treasure, 'v2'))
v2_blueprint.add_url_rule('/api/v1/category/monsters', view_func=load_view(view_funcs.monsters, 'v1'))
v2_blueprint.add_url_rule('/api/v2/category/monsters', view_func=load_view(view_funcs.monsters, 'v2'))
v2_blueprint.add_url_rule('/api/v1/category/materials', view_func=load_view(view_funcs.materials, 'v1'))
v2_blueprint.add_url_rule('/api/v2/category/materials', view_func=load_view(view_funcs.materials, 'v2'))
v2_blueprint.add_url_rule('/api/v1/category/equipment', view_func=load_view(view_funcs.equipment, 'v1'))
v2_blueprint.add_url_rule('/api/v2/category/equipment', view_func=load_view(view_funcs.equipment, 'v2'))
v2_blueprint.add_url_rule('/api/v1/category/creatures', view_func=load_view(view_funcs.creatures, 'v1'))
v2_blueprint.add_url_rule('/api/v2/category/creatures', view_func=load_view(view_funcs.creatures, 'v2'))

if __name__ == '__main__':  
    app = flask.Flask(__name__, static_folder='compendium/images')
    CORS(app)
    app.register_error_handler(500, lambda ctx: ({'data': {}, 'message': 'Server error'}, 500))
    app.register_error_handler(404, lambda ctx: ({'data': {}, 'message': 'Not found'}, 404))
    app.register_blueprint(v2_blueprint)
    app.run(debug=True)