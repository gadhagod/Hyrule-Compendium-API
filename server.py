
from src import view_funcs
import flask
from flask_cors import CORS

app = flask.Flask(__name__, static_folder='compendium/images')
CORS(app)

app.add_url_rule('/api/<version>', view_func=view_funcs.all)

app.add_url_rule('/api/<version>/entry/<inp>', view_func=view_funcs.entry)
app.add_url_rule('/api/<version>/entry/<inp>/image', view_func=view_funcs.entry_image)
app.add_url_rule('/api/<version>/master_mode/entry/<inp>', view_func=view_funcs.master_mode_entry)

app.add_url_rule('/api/<version>/category/treasure', view_func=view_funcs.treasure)
app.add_url_rule('/api/<version>/category/monsters', view_func=view_funcs.monsters)
app.add_url_rule('/api/<version>/category/materials', view_func=view_funcs.materials)
app.add_url_rule('/api/<version>/category/equipment', view_func=view_funcs.equipment)
app.add_url_rule('/api/<version>/category/creatures', view_func=view_funcs.creatures)
app.add_url_rule('/api/<version>/master_mode', view_func=view_funcs.all_master_mode)

@app.route('/')
@app.route('/api')
def website():
    return flask.redirect('https://gadhagod.github.io/Hyrule-Compendium-API')

app.register_error_handler(500, lambda ctx: {'data': {}, 'message': 'Server error'})

if __name__ == '__main__':  
    app.run()