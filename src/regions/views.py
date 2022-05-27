from rockset import F
from ..utils import region_query, no_results

def get_category(category_name):
    data = region_query(F['name'] == category_name.title())
    if(data):
        return {'data': data[0]}
    return no_results

def get_all():
    return {'data': region_query()}