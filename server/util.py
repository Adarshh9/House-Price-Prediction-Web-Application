import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_price(area ,location ,bedrooms ,lift ,carPark):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = 4
    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = bedrooms
    x[2] = lift
    x[3] = carPark
    
    if loc_index >= 0:
        x[loc_index] = 1
        
    return round(__model.predict([x])[0] , 2)

def get_location_names():
    return __location

def load_saved_artifacts():
    print("Loading save artifacts...start")
    global __location
    global __data_columns
    global __model
    
    with open('./artifacts/columns.json' , 'r') as file:
        __data_columns = json.load(file)["data_columns"]
        __location = __data_columns[4:]
        
    with open("./artifacts/mumbai_home_price_prediction_model.pickle" , "rb") as file:
        __model  = pickle.load(file)
        
    print("Loading save artifacts...Done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names()) 
    
    print(get_estimated_price(1000 , "Bhiwandi" , 2 , 1 , 1))
    print(get_estimated_price(1000 , "Borivali East", 2 , 1 ,1))
    print(get_estimated_price(1000 , "Jamnagar" , 2 , 1 , 1))
    print(get_estimated_price(1000 , "New York" , 2 , 1 , 1))