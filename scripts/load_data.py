# should be run from root dir
# creates db (if needed) and adds/updates data in the db
# see "self hosting" for information

from sys import argv
from os import getenv, getcwd, listdir, path
from requests import post, get
from json import dumps, loads

if not getenv('RS2_TOKEN'):
    raise Exception("Api key not provided as RS2_TOKEN env var")

root_dir = getcwd()
base_url = f'https://{getenv("RS2_SERVER") or "api.rs2.usw2.rockset.com"}'
api_key = f'ApiKey {getenv("RS2_TOKEN") or argv[1]}'

def get_files_in_dir(dir_path):
    res = []
    for file in listdir(dir_path):
        file_loc = f'{dir_path}/{file}'
        if path.isfile(file_loc) and file_loc.endswith('.json'):
            res.append((file_loc, file.replace('.json', '')))
        elif path.isdir(file_loc):
            res += get_files_in_dir(file_loc)
    return res

def collection_exists(workspace, collection_name):
    return get(
        f'{base_url}/v1/orgs/self/ws/{workspace}/collections/{collection_name}',
        headers={'Authorization': api_key, 'Content-Type': 'application/json'}
    ).status_code == 200

def workspace_exists(workspace_name):
    return get(
        f'{base_url}/v1/orgs/self/ws/{workspace_name}',
        headers={'Authorization': api_key, 'Content-Type': 'application/json'}
    ).status_code == 200
    
def create_collection(workspace, collection_name, ingest_transformation):
    if (collection_exists(workspace, collection_name)):
        print(f'Collection {workspace}.{collection_name} already exists... skipping creation.')
        return
    print(f'Creating collection {workspace}.{collection_name}')
    res = post(f'{base_url}/v1/orgs/self/ws/{workspace}/collections', dumps({
        'field_mapping_query': {'sql': ingest_transformation},
        'name': collection_name
    }), headers={'Authorization': api_key, 'Content-Type': 'application/json'})
    if (res.status_code != 200):
        raise Exception(res.text)

def create_workspace(workspace_name):
    if (workspace_exists(workspace_name)):
        print(f'Workspace {workspace_name} already exists... skipping creation.')
        return
    print(f'Creating workspace {workspace_name}')
    res = post(f'{base_url}/v1/orgs/self/ws', dumps({
        'name': workspace_name
    }), headers={'Authorization': api_key, 'Content-Type': 'application/json'})
    if (res.status_code != 200):
        raise Exception(res.text)
        
def add_docs(workspace, collection, docs):
    print(f'Adding data to {workspace}.{collection}')
    res = post(f'{base_url}/v1/orgs/self/ws/{workspace}/collections/{collection}/docs', dumps({
        'data': loads(docs)
    }), headers={'Authorization': api_key, 'Content-Type': 'application/json'})
    if (res.status_code != 200):
        raise Exception(res.text)
        
def initialize_botw_workspace():
    create_workspace('botw-api-v3')
    
def initialize_totk_workspace():
    create_workspace('totk-api-v3')

def initialize_botw_collections():
    compendium_ingest_tranformation = open(f'{root_dir}/db/botw/mappings/compendium.sql', 'r').read()
    regions_ingest_tranformation = open(f'{root_dir}/db/botw/mappings/region.sql', 'r').read()
    create_collection('botw-api-v3', 'creatures', compendium_ingest_tranformation)
    create_collection('botw-api-v3', 'equipment', compendium_ingest_tranformation)
    create_collection('botw-api-v3', 'materials', compendium_ingest_tranformation)
    create_collection('botw-api-v3', 'monsters', compendium_ingest_tranformation)
    create_collection('botw-api-v3', 'treasure', compendium_ingest_tranformation)
    create_collection('botw-api-v3', 'master_mode', compendium_ingest_tranformation)
    create_collection('botw-api-v3', 'regions', regions_ingest_tranformation)
    
def initialize_totk_collections():
    create_collection('totk-api-v3', 'creatures', open(f'{root_dir}/db/totk/mappings/creatures.sql', 'r').read())
    create_collection('totk-api-v3', 'equipment', open(f'{root_dir}/db/totk/mappings/equipment.sql', 'r').read())
    create_collection('totk-api-v3', 'materials', open(f'{root_dir}/db/totk/mappings/materials.sql', 'r').read())
    create_collection('totk-api-v3', 'monsters', open(f'{root_dir}/db/totk/mappings/monsters.sql', 'r').read())
    create_collection('totk-api-v3', 'treasure', open(f'{root_dir}/db/totk/mappings/treasure.sql', 'r').read())
    
def load_botw_data():
    files = get_files_in_dir(f'{root_dir}/db/botw/data')
    for file in files:
        add_docs('botw-api-v3', file[1], open(file[0], 'r').read())
    
def load_totk_data():
    files = get_files_in_dir(f'{root_dir}/db/totk/data/compendium')
    for file in files:
        add_docs('totk-api-v3', file[1], open(file[0], 'r').read())
        
initialize_botw_workspace()
initialize_totk_workspace()
initialize_botw_collections()
initialize_totk_collections()
load_botw_data()
load_totk_data()