import json
import joblib
import numpy as np

__locations = None
__model = None
__area_type = None
data_columns = None


def get_estimated_price(size, total_sqft, balcony, location, area_type):
    x = np.zeros(len(data_columns))
    x[0] = size
    x[1] = total_sqft
    x[2] = balcony
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1
    try:
        area_index = data_columns.index(area_type.lower())
    except:
        area_index = -1
    if loc_index >= 0:
        x[loc_index] = 1
    if area_index >= 0:
        x[area_index] = 1
    print(f"size: {size}, total_sqft: {total_sqft}, balcony:{balcony}, location:{location}, area_type:{area_type}")
    return round(__model.predict([x])[0], 2)


def get_locations():
    return __locations


def get_area_type():
    return __area_type


def load_artifacts():  # Loading artifacts in a separate function will reduce the computation because the file will not be loaded each time you call the other functions (If you have loaded the files in the other functions instead of creating this function)
    global __model
    with open('./artifacts/Ridge_Model', 'rb') as f:
        __model = joblib.load(f)
    global __locations
    global __area_type
    global data_columns
    with open('./artifacts/columns.json', 'r') as f:
        data_columns = json.load(f)['columns']
        __locations = data_columns[3:187]
        __area_type = data_columns[187:]


load_artifacts()
#get_locations()
#get_area_type()
# print(__locations)
# print(__area_type)
# print(get_estimated_price(2, 2000, 1, "6th phase jp nagar", "area_type_carpet  area"))
# print(get_estimated_price(3, 2000, 1, "6th phase jp nagar", "area_type_carpet  area"))
