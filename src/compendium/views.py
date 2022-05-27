from . import main
from rockset import F

def treasure():
    return {'data': main.get_category('treasure')}

def monsters():
    return {'data': main.get_category('monsters')}

def materials():
    return {'data': main.get_category('materials')}

def equipment():
    return {'data': main.get_category('equipment')}

def creatures():
    return {'data': main.get_category('creatures')}

def entry(inp):
    res = main.get_entry((F['id'] == int(inp)) if inp.isnumeric() else F['name'] == inp.lower().replace('_', ' '))
    return main.no_results if not res else {'data': res[1]}

entry_image = main.get_entry_image

def all():
    return {'data': main.get_all()}

def master_mode_entry_image(inp):
    return main.get_entry_image(inp, master_mode=True)

def master_mode_entry(inp):
    res = main.get_master_mode_entry(inp)
    return ({'data': res[0]} if res else main.no_results)

def all_master_mode():
    return {'data': main.get_all_master_mode_entries()}