from typing import Optional, Union
from ..src.types import *
from os import getenv
from flask import send_from_directory, Response
from rockset import Client, Q, F
from sys import argv

rs = Client(api_key=getenv('RS2_TOKEN') or argv[1], api_server='api.rs2.usw2.rockset.com')

selects = {
    'treasure': ['drops'],
    'monsters': ['drops'],
    'materials': ['cooking_effect', 'hearts_recovered'],
    'equipment': ['attack', 'defense'],
    'creatures': {
        'food': ['hearts_recovered', 'cooking_effect'],
        'others': ['drops']
    }
}

entry_not_found = {'data': {}, 'message': 'no results'}, 404

def query(
    category: Union[StandardCategoryName, DlcCategoryName],
    where: Optional[bool]=None,
    select: list[BaseEntrySelect]=[]
) -> list[EntryData]: return rs.sql(
    Q(f'botw-api.{category}')
        .where(where if where is not None else F['id'].is_not_null())
        .select(*[
            'id', 
            'name', 
            'description', 
            'common_locations', 
            'image', 
            'category'
        ]+list(map(lambda i: F[i], select)))
).results()

def get_category(version: VersionString, category: StandardCategoryName) -> CategoryData:
    return {'non_food' if version == 'v2' else 'non-food': query(
        category='creatures', 
        where=F['cooking_effect'].is_null(), 
        select=selects['creatures']['others']
    ), 'food': query(
        category='creatures', 
        where=F['cooking_effect'].is_not_null(), 
        select=selects['creatures']['food']
    )} if category == "creatures" else query(category=category, select=selects[category])

def get_entry(where) -> tuple[StandardCategoryName, EntryData]:
    for category in list(selects.keys())[:-1]:
        res = query(
            category=category, 
            where=where, 
            select=selects[category]
        )
        if res:
            return category, res[0]

    res = query(
        category='creatures',
        where=where,
        select=['hearts_recovered', 'cooking_effect']
    )

    if res:
        if res[0]['cooking_effect'] is None:
            res = query(
                category='creatures',
                where=where,
                select=['drops']
            )
        return 'creatures', res[0]

def get_entry_image(version, inp, master_mode=False) -> Union[Response, tuple[dict, int]]:
    if inp == "master_mode":
        return entry_not_found

    target_entry = None
    if master_mode:
        if inp.isnumeric():
            res = query(
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
                res = query(
                    category=category,
                    where=(F['_id'] == inp),
                )
                if res:
                    target_entry = res[0]['name']
                    break
        else:
            target_entry = inp

    if not target_entry:
        return entry_not_found

    try:
        return send_from_directory(f'compendium/images{"/master_mode" if master_mode else ""}', f"{target_entry.replace(' ', '_').replace('+', '＋')}.png", mimetype='image/png')
    except FileNotFoundError:
        return entry_not_found

def get_all(version) -> list[CategoryData]:
    category_metadata = {}
    for category in selects.keys():
        category_metadata[category] = get_category(version, category)
    return category_metadata

def get_master_mode_entry(version, inp) -> EntryData:
    name, id = ("", int(inp)) if inp.isnumeric() else (inp.replace('_', " "), 0)
    return query(
        category='master_mode',
        where=(F['name'] == name) | (F['id'] == id),
        select=selects['monsters']
    )

def get_all_master_mode_entries(version) -> list[EntryData]:
    return query(
        category='master_mode',
        select=selects['monsters']
    )