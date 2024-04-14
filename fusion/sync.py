from typing import List
import pymongo
import pandas as pd

def import_merge_data(ageimpulse: str, clients_collection: List[str], output_file: str):
               # Connexion à MongoDB
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client[ageimpulse] 
    
    
    dataframes = []
    for clients in clients_collection:
        clients_collection = db[clients]  
        cursor = clients_collection.find()  
        df = pd.DataFrame(list(cursor)) 
        dataframes.append(df)
    
    # La Fusion
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    
    merged_df.to_csv(output_file, index=False)
    print(f"Les données ont été fusionnées {output_file}")

if __name__ == "__main__":
    database_name = 'ageimpulse' 
    collection_names = ['clients', 'devices', 'users'] 
    output_file = 'merged_data.csv' 
    
    import_merge_data(database_name, collection_names, output_file)
