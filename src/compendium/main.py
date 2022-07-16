from typing import Union
from os import getenv
from flask import send_from_directory, Response
from rockset import Client, Q, F
from sys import argv
from ..utils import compendium_query, no_results
from ..types import *

rs = Client(api_key=getenv('RS2_TOKEN') or argv[1], api_server='api.rs2.usw2.rockset.com')

selects = {
    'treasure': ['drops'],
    'monsters': ['drops'],
    'materials': ['cooking_effect', 'hearts_recovered'],
    'equipment': ['attack', 'defense'],
    'creatures': {
        'edible': ['hearts_recovered', 'cooking_effect', 'edible'],
        'not_edible': ['drops', 'edible']
    }
}

def get_category(category: StandardCategoryName) -> CategoryData:
    if category == 'creatures':
        return (
            compendium_query(category='creatures', where=F['edible'] == True, select=selects['creatures']['edible'])
            + compendium_query(category='creatures', where=F['edible'] == False, select=selects['creatures']['not_edible'])
        )
    return compendium_query(category=category, select=selects[category])

def get_entry(where) -> tuple[StandardCategoryName, EntryData]:
    for category in list(selects.keys())[:-1]:
        res = compendium_query(
            category=category, 
            where=where, 
            select=selects[category]
        )
        if res:
            return category, res[0]

    res = compendium_query(
        category='creatures',
        where=where,
        select=selects['creatures']['edible'] + selects['creatures']['not_edible']
    )

    if res:
        if res[0]['edible']:
            res[0].pop("drops", None)
        else:
            res[0].pop("hearts_recovered", None)
            res[0].pop("cooking_effect", None)
        return 'creatures', res[0]

def get_entry_image(inp, master_mode=False) -> Union[Response, tuple[dict, int]]:
    if inp == "master_mode":
        return no_results

    target_entry = None
    if master_mode:
        if inp.isnumeric():
            res = compendium_query(
                category='master_mode',
                where=(F['_id'] == inp),
            )
            if res:
                target_entry = res[0]['name']
        else:
            target_entry = inp
    else:
        if inp.isnumeric():
            for category in selects.keys():
                res = compendium_query(
                    category=category,
                    where=(F['_id'] == inp),
                )
                if res:
                    target_entry = res[0]['name']
                    break
        else:
            target_entry = inp

    if not target_entry:
        return no_results

    try:
        return send_from_directory(f'db/data/compendium/images{"/master_mode" if master_mode else ""}', f"{target_entry.replace(' ', '_').replace('+', '＋')}.png", mimetype='image/png')
    except FileNotFoundError:
        return no_results

def get_all() -> list[CategoryData]:
    category_metadata = {}
    for category in selects.keys():
        category_metadata[category] = get_category(category)
    return category_metadata

def get_master_mode_entry(inp) -> EntryData:
    name, id = ("", int(inp)) if inp.isnumeric() else (inp.replace('_', " "), 0)
    return compendium_query(
        category='master_mode',
        where=(F['name'] == name) | (F['id'] == id),
        select=selects['monsters']
    )

def get_all_master_mode_entries() -> list[EntryData]:
    return compendium_query(
        category='master_mode',
        select=selects['monsters']
    )