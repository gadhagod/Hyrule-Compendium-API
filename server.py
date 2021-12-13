from imghdr import what
from os import getenv
from json import loads, dumps
import flask
from rockset import Client, Q
from flask_cors import CORS
from sys import argv

app = flask.Flask(__name__, static_folder='compendium/images')
CORS(app)
rs = Client(api_key=getenv('RS2_TOKEN') or argv[1], api_server='api.rs2.usw2.rockset.com')

selects = {
    'treasure': 'drops',
    'monsters': 'drops',
    'materials': 'cooking_effect, hearts_recovered',
    'equipment': 'attack, defense'
}
creatures_selects = {
    'food': 'hearts_recovered, cooking_effect',
    'others': 'drops'
}

def creatures_category(version):
    others = list(
        rs.sql(
            Q(
                'select id, name, description, common_locations, image, category, {} from "botw-api".creatures where cooking_effect is null'.format(creatures_selects['others'])
            )
        )
    )
    foods = list(
        rs.sql(
            Q(
                'select id, name, description, common_locations, image, category, {} from "botw-api".creatures where cooking_effect is not null'.format(creatures_selects['food'])
            )
        )
    )
    if version == 'v1':
        food_key = 'non-food'
    elif version == 'v2':
        food_key = 'non_food'
    return {food_key: others, 'food': foods}

def single_category(category):
    query = 'select id, name, description, common_locations, image, category, {} from "botw-api".{}'.format(selects[category], category)
    return list(
        rs.sql(Q(query))
    )

def id_name_query(target, where):
    target = target.replace('\'', '\'\'')
    for category in list(selects.keys()):
        res = list(rs.sql(Q('select id, name, description, common_locations, image, category, {} from "botw-api".{} where {}=\'{}\''.format(selects[category], category, where, target))))
        if res != []:
            return category, res[0]

    res = list(rs.sql(Q('select id, name, description, hearts_recovered, category, cooking_effect, common_locations, image from "botw-api".creatures where {}=\'{}\''.format(where, target))))
    if res != []:
        if res[0]['cooking_effect'] == None:
            res = list(rs.sql(Q('select id, name, description, drops, common_locations, image, category from "botw-api".creatures where {}=\'{}\''.format(where, target))))
        return 'creatures', res[0]
    return None

def all(version):
    category_metadata = {}
    for category in selects.keys():
        category_metadata[category] = single_category(category)
    category_metadata['creatures'] = creatures_category(version)

    return {'data': category_metadata}

def entry(version, inp):
    try:
        try:
            int(inp)
            cat, query_res = id_name_query(inp, '_id')
            return {'data': query_res}
        except ValueError:
            cat, query_res = id_name_query(inp.lower().replace('_', ' '), 'name')
            return {'data': query_res}
    except TypeError:
        return {'data': {}, 'message': 'no results'}, 404

def img_entry(version, inp):
    try:
        try: # inp is ID
            _, query_res = id_name_query(int(inp), '_id')
            target_entry = query_res['name'].replace(' ', '_').replace('＋', '')
        except ValueError: # inp is name
            target_entry = inp.replace(' ', '_').replace('+', '＋')
        
        print(target_entry)
        return flask.send_from_directory('compendium/images', target_entry, mimetype=f'image/{what(f"compendium/images/{target_entry}")}')
    except TypeError:
        return {'data': {}, 'message': 'no results'}, 404

def treasure(version):
    return {'data': single_category('treasure')}

def monsters(version):
    return {'data': single_category('monsters')}

def materials(version):
    return {'data': single_category('materials')}

def equipment(version):
    return {'data': single_category('equipment')}

def creatures(version):
    return {'data': creatures_category(version)}

@app.route('/api/<version>')
def prod_all(version):
    res = all(version)
    return(res)

@app.route('/api/<version>/entry/<inp>/image')
def entry_img(version, inp):
    return(img_entry(version, inp))

@app.route('/api/<version>/entry/<inp>')
def prod_entry(version, inp):
    res = entry(version, inp)
    return(res)

@app.route('/api/<version>/category/treasure')
def prod_treasure(version):
    res = treasure(version)
    return(res)

@app.route('/api/<version>/category/monsters')
def prod_monsters(version):
    res = monsters(version)
    return(res)

@app.route('/api/<version>/category/materials')
def prod_materials(version):
    res = materials(version)
    return(res)

@app.route('/api/<version>/category/equipment')
def prod_equipment(version):
    res = equipment(version)
    return(res)

@app.route('/api/<version>/category/creatures')
def prod_creatures(version):
    res = creatures(version)
    return(res)

@app.route('/')
@app.route('/api')
def home():
    return flask.redirect('https://gadhagod.github.io/Hyrule-Compendium-API')

app.register_error_handler(500, lambda ctx: {"data": {}, "message": "Server error"})

if __name__ == '__main__': 
    app.run()