from ..src import utils
from rockset import F

def treasure(version):
    return {'data': utils.get_category(version, 'treasure')}

def monsters(version):
    return {'data': utils.get_category(version, 'monsters')}

def materials(version):
    return {'data': utils.get_category(version, 'materials')}

def equipment(version):
    return {'data': utils.get_category(version, 'equipment')}

def creatures(version):
    return {'data': utils.get_category(version, 'creatures')}

def entry(version, inp):
    res = utils.get_entry((F['id'] == int(inp)) if inp.isnumeric() else F['name'] == inp.lower().replace('_', ' '))
    return utils.entry_not_found if not res else {'data': res[1]}

entry_image = utils.get_entry_image

def all(version):
    return {'data': utils.get_all(version)}

def master_mode_entry_image(version, inp):
    return utils.get_entry_image(version, inp, master_mode=True)

def master_mode_entry(version, inp):
    res = utils.get_master_mode_entry(version, inp)
    return ({'data': res[0]} if res else utils.entry_not_found)

def all_master_mode(version):
    return {'data': utils.get_all_master_mode_entries(version)}