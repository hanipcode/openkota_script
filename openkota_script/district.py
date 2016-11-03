import csv


DISTRICT_FILE = open('csv/districts.csv')
DISTRICT_READER = csv.reader(DISTRICT_FILE)
DISTRICT_LIST = list(DISTRICT_READER)


def get_all_district_name():
    """
    function get_all_district_name
    return a list of every district name
    """
    result = []
    for district_row in DISTRICT_LIST:
        district_name = district_row[2]
        result.append(district_name)
    return result

def get_all_district_data():
    """
    function get_all_district_data
    return a dictionary of relation beetween district and id
    """
    result = []
    for district_row in DISTRICT_LIST:
        res = {}
        district_id = district_row[0]
        district_regency_id = district_row[1]
        district_name = district_row[2]
        res['district_id'] = district_id
        res['district_regency_id'] = district_regency_id
        res['district_name'] = district_name
        result.append(res)
    return result
