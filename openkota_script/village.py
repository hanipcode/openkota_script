import csv

VILLAGE_FILE = open('csv/villages.csv')
VILLAGE_READER = csv.reader(VILLAGE_FILE)
VILLAGE_LIST = list(VILLAGE_READER)

def get_all_village_name():
    """
    function get_all_village_name 
    return a list of all village name
    """
    result = []
    for village_row in VILLAGE_LIST:
        village_name = village_row[2]
        result.append(village_name)
    return result

def get_all_village_data():
    """
    function get_all_village_data
    return a dictionary of relation beetween village and
    district_id and vilage_id
    """
    result = []
    for village_row in VILLAGE_LIST:
        res = {}
        village_id = village_row[0]
        village_district_id = village_row[1]
        village_name = village_row[2]
        res['village_id'] = village_id
        res['village_district_id'] = village_district_id
        res['village_name'] = village_name
        result.append(res)
    return result
