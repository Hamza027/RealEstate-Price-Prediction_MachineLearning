import numpy as np
import pickle
import json

def get_location_names():
    return __locations

def get_price_prediction(sqft,bath,balcony,bhk,area):
    x = [None]*7
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk

    if area == "Built-up":
        x[4]=0
        x[5]=0
        x[6]=0
        
        return np.round(__model.predict([x]),2).tolist()
    elif area == "Carpet":
        x[4]=1
        x[5]=0
        x[6]=0
        
        return (np.round(__model.predict([x]),2)).tolist()
        
    elif area == "Plot":
        x[4]=0
        x[5]=1
        x[6]=0
        
        return (np.round(__model.predict([x]),2)).tolist()
        
    elif area == "Super":
        x[4]=0
        x[5]=0
        x[6]=1
        
        return np.round(__model.predict([x]),2).tolist()
    

def load_save_artifacts():
    print("loading saved artifacts ... start")
    global __data_columns
    global __locations

    with open("/Users/hamza/DataSc_RM/MachineLearning/Proj_RealEstatePricePred/server/artifacts/columns.json",'r') as f:
        __data_columns= json.load(f)["data_columns"]
        __locations = __data_columns[3:]
    global __model
    with open ("/Users/hamza/DataSc_RM/MachineLearning/Proj_RealEstatePricePred/server/artifacts/home_prices_model.pickle","rb") as f:
        __model = pickle.load(f)


if __name__ == "__main__":
    load_save_artifacts()
    print(get_location_names())
    print(get_price_prediction(3500.0,2.0,2.0,2,"Plot",))