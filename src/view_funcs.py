from src import utils

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
    try:
        try:
            int(inp)
            res = utils.get_entry(inp, '_id')[1]
        except ValueError:
            res = utils.get_entry(inp.lower().replace('_', ' '), 'name')[1]
        return {'data': res}
    except TypeError:
        return utils.entry_not_found

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