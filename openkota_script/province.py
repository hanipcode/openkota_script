import csv

PROVINCE_FILE = open('csv/provinces.csv')
PROVINCE_READER = csv.reader(PROVINCE_FILE)
PROVINCE_LIST = list(PROVINCE_READER)


def get_all_province_name():
    """
    function get_all_province_name
    return a list of available province name
    """
    result = []
    for province_row in PROVINCE_LIST:
        province_name = province_row[1]
        result.append(province_name)
    return result

def get_all_province_id():
    """
    function get_all_province_id
    return a list of available province id
    """
    result = []
    for province_row in PROVINCE_LIST:
        province_id = province_row[0]
        result.append(province_id)
    return result

def get_all_province_data():
    """
    function get_all_province_data
    return a dictionary with data[province_id] = province_name
    dictionray provide a better relation beetween id and province
    """
    result = {}
    for province_row in PROVINCE_LIST:
        province_id = province_row[0]
        province_name = province_row[1]
        result[province_name] = province_id
    return result
