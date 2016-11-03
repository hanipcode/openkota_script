import csv

REGENCY_FILE = open('csv/regencies.csv')
REGENCY_READER = csv.reader(REGENCY_FILE)
REGENCY_LIST  = list(REGENCY_READER)

def get_all_regency_name():
    """
    fucntin get_all_regency_name
    return a list of regency name
    """
    result = []
    for regency_row in REGENCY_LIST:
        regency_name = regency_row[2]
        result.append(regency_name)
    return result

def get_all_regency_data():
    """
    function get_all_regency_data
    return 2 dictionary 
    """
    result = []
    for regency_row in REGENCY_LIST:
        res = {}
        regency_id = regency_row[0]
        regency_province_id = regency_row[1]
        regency_name  = regency_row[2]
        res['regency_id'] = regency_id
        res['regency_province_id'] = regency_province_id
        res['regency_name'] = regency_name
        result.append(res)
    return result
