from typing import Optional, Union
import flask
from src.types import *
from os import getenv
from rockset import Client, Q, F
from sys import argv

rs = Client(api_key=getenv('RS2_TOKEN') or argv[1], api_server='api.rs2.usw2.rockset.com')

def entry_query(
    category: Union[StandardCategoryName, DlcCategoryName],
    where: Optional[bool]=None,
    select: list[BaseEntrySelect]=[]
) -> list[EntryData]: return rs.sql(
    Q(f'botw-api-v3.{category}')
        .where(where if where is not None else F['id'].is_not_null())
        .select(*[
            'id', 
            'name', 
            'description', 
            'common_locations', 
            'image', 
            'category',
            'dlc'
        ]+list(map(lambda i: F[i], select)))
).results()

def region_query(
    where=None
) -> list[EntryData]: 
    return (rs.sql(
        Q(f'botw-api-v3.regions')
            .where(where)
            .select(
                'name', 
                'regular_shrines', 
                'dlc_shrines', 
                'settlements' 
            )
    ) if where else rs.sql(
        Q(f'botw-api.regions')
            .select(
                'name', 
                'regular_shrines', 
                'dlc_shrines', 
                'settlements' 
            ))
    ).results()

def redirectToDocs():
    return flask.redirect('https://gadhagod.github.io/Hyrule-Compendium-API')

no_results = {'data': {}, 'message': 'no results'}, 404