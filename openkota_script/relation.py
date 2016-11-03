from province import *
from regency import *
from district import *
from village import *

PROVINCE_DATA = get_all_province_data()
REGENCY_DATA = get_all_regency_data()
DISTRICT_DATA = get_all_district_data()
VILLAGE_DATA = get_all_village_data()

def get_province_id(name):
    """
    function get_province_id
    return the province id of specified province
    """
    return PROVINCE_DATA[name]

def get_regencies_by_province(name):
    """
    function get_regencies_by_province
    return a list of regencies in the specified province
    """
    result = []
    done_search = False
    province_id = get_province_id(name)
    for regency in REGENCY_DATA:
        if province_id == regency['regency_province_id']:
            done_search = True
            result.append(regency)
        elif province_id != regency['regency_province_id'] and done_search:
            break;
    return result


def get_districts_by_province(name):
    """
    function get_regency_in_province
    return a list of district in the specified province
    """
    result = []
    done_search = False
    province_id = get_province_id(name)
    for district in DISTRICT_DATA:
        district_province_id = district['district_id'][:2]
        if district_province_id == province_id:
            result.append(district)
        elif district_province_id != province_id and done_search:
            break;
    return result

def get_village_by_province(name):
    """
    function get_village_by_province
    return a list of village in the specified province
    """
    result = []
    done_search = False
    province_id = get_province_id(name)
    for village in VILLAGE_DATA:
        village_province_id = village['village_id'][:2]
        if village_province_id == province_id:
            done_search = True
            result.append(village)
        elif village_province_id != province_id and done_search:
            break;
    return result

def get_regency_id(name):
    """
    function get_regency_id
    return an id of the specified regency name
    """
    for regency in REGENCY_DATA:
        if regency['regency_name'] == name:
            return regency['regency_id']
    return 'unknown regency'

        
def get_districts_by_regency(name):
    """
    function get_districts_by_regency
    return a list of district in the specified regency
    """
    result = []
    done_search = False
    regency_id = get_regency_id(name)
    for district in DISTRICT_DATA:
        if regency_id == district['district_regency_id']:
            result.append(district)
            done_search = True
        elif regency_id != district['district_regency_id'] and done_search:
            break
    return result

def get_district_id(name):
    """
    function get_district_id
    return an id of the specified district name
    """
    for district in DISTRICT_DATA:
        if district['district_name'] == name:
            return district['district_id']
    return 'unknown district'

def get_villages_by_district(name):
    """
    function get_vilages_by_district
    return a list of villages in the specified district
    """
    result = []
    done_search = False
    district_id = get_district_id(name)
    for village in VILLAGE_DATA:
        if district_id == village['village_district_id']:
            done_search = True
            result.append(village)
        elif district_id != village['village_district_id'] and done_search:
            break
    return result

