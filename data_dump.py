import pymongo
import pandas as pd
import json

#*Mongodb localhost url for established connection with python
client = pymongo.MongoClient("mongodb+srv://sp27:be990396@cluster0.hinrq6i.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = r"C:\Users\shara\ML_Projects\DATA_Download\aps_failure_training_set1.csv"
DATABASE_NAME = "APS"
COLLECTION_NAME = "Sensor"

if __name__ == "__main__":
    #*CSV to DataFrame
    df = pd.read_csv(DATA_FILE_PATH) 
    print(f"Rows and Columns: {df.shape}")
    
    #*deleting the index column
    df.reset_index(drop=True, inplace=True) 
    
    #**Converting DataFrame to JSON for transferring to MongoDB**
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    #**Pushsing json records to MongoDB**
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record) 
    
   




