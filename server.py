from os import getenv
from json import loads
import flask
from rockset import Client, Q
from flask_cors import CORS

app = flask.Flask(__name__, template_folder='js')
CORS(app)
rs = Client(api_key=getenv('RS2_TOKEN'), api_server='api.rs2.usw2.rockset.com')

def redirect(link):
    return '<script>window.location.replace("{}")</script>'.format(link)

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
                'select id, name, description, {} from "botw-api".creatures where cooking_effect is null'.format(creatures_selects['others'])
            )
        )
    )
    foods = list(
        rs.sql(
            Q(
                'select id, name, description, {} from "botw-api".creatures where cooking_effect is not null'.format(creatures_selects['food'])
            )
        )
    )
    if version == 'v1':
        food_key = 'non-food'
    elif version == 'v2':
        food_key = 'non_food'
    return {food_key: others, 'food': foods}

def single_category(category):
    query = 'select id, name, description, common_locations, {} from "botw-api".{}'.format(selects[category], category)
    return list(
        rs.sql(Q(query))
    )

def id_name_query(target, where):

    for category in list(selects.keys()):
        print('select id, name, description, {} from "botw-api".{} where {}=\'{}\''.format(selects[category], category, where, target))
        res = list(rs.sql(Q('select id, name, description, {} from "botw-api".{} where {}=\'{}\''.format(selects[category], category, where, target.replace('\'', '\'\'')))))
        if res != []:
            return category, res[0]

    res = list(rs.sql(Q('select id, name, description, hearts_recovered, cooking_effect from "botw-api".creatures where {}=\'{}\''.format(where, target))))
    if res != []:
        if res[0]['cooking_effect'] == None:
            res = list(rs.sql(Q('select id, name, description, drops from "botw-api".creatures where {}=\'{}\''.format(where, target))))
        return 'creatures', res[0]
    return None

@app.route('/api/<version>')
def all(version):
    category_metadata = {}
    for category in selects.keys():
        category_metadata[category] = single_category(category)
    category_metadata['creatures'] = creatures_category(version)
    return {'data': category_metadata}

@app.route('/api/<version>/entry/<inp>')
def entry(version, inp):
    try:
        try:
            int(inp)
            cat, query_res = id_name_query(inp, '_id')
            query_res['category'] = cat
            return {'data': query_res}
        except ValueError:
            cat, query_res = id_name_query(inp.lower().replace('_', ' '), 'name')
            query_res['category'] = cat
            return {'data': query_res}
    except TypeError:
        return {'data': {}, 'message': 'no results'}

@app.route('/api/<version>/category/treasure')
def treasure(version):
    return {'data': single_category('treasure')}

@app.route('/api/<version>/category/monsters')
def monsters(version):
    return {'data': single_category('monsters')}

@app.route('/api/<version>/category/materials')
def materials(version):
    return {'data': single_category('materials')}

@app.route('/api/<version>/category/equipment')
def equipment(version):
    return {'data': single_category('equipment')}

@app.route('/api/<version>/category/creatures')
def creatures(version):
    return {'data': creatures_category(version)}

@app.route('/issues')
@app.route('/bugs')
@app.route('/suggestions')
def issues():
    return redirect('https://github.com/gadhagod/Hyrule-Compendium-API/issues')

@app.route('/')
@app.route('/api')
def home():
    return redirect('https://github.com/gadhagod/Hyrule-Compendium-API')

if __name__ == '__main__':
    app.run()